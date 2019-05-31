from django.contrib import admin
from .models import Friends, Comment




class CommentOption(admin.ModelAdmin):
    list_display = ['id', 'friend', 'comment_contents']
    list_filter = ['friend', 'comment_contents']

class CommentInline(admin.TabularInline):
    model = Comment

class FriendOptions(admin.ModelAdmin):

    list_display = ['user', 'friend_name', 'friend_mobile', 'friend_group', 'friend_memo']
    list_filter = ['user','friend_name', 'friend_mobile', 'friend_group','friend_memo']
    search_fields = ['friend_name', 'friend_mobile', 'friend_group', 'friend_memo']
    inlines = [CommentInline]


admin.site.register(Friends, FriendOptions)
admin.site.register(Comment, CommentOption)
