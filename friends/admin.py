from django.contrib import admin
from .models import Friends, Comment

class FriendOptions(admin.ModelAdmin):

    list_display = ['id', 'friend_name', 'friend_mobile', 'friend_group', 'friend_memo']
    list_filter = ['friend_name', 'friend_mobile', 'friend_group','friend_memo']
    search_fields = ['friend_name', 'friend_mobile', 'friend_group', 'friend_memo']

admin.site.register(Friends, FriendOptions)

class CommentOption(admin.ModelAdmin):
    list_display = ['id', 'friend', 'comment_contents']
    list_filter = ['friend', 'comment_contents']

admin.site.register(Comment, CommentOption)
