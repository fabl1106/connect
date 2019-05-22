from django.urls import path

from friends.models import Friends
from .views import FriendCreate, FriendDelete, FriendDetail, FriendUpdate, FriendDetail1, FriendConnect, \
    comment_write, friends_listall, FriendWeekList, FriendMonthList, comment_update, comment_delete, Main, \
    FriendTodayList

app_name = 'friend'
urlpatterns = [
    path('detail/comment/<int:pk>/', comment_write, name='comment'),
    path('comment/delete/<int:pk>/', comment_delete, name="comment_delete"),
    path('comment/update/<int:pk>/', comment_update, name="comment_update"),
    path('monthlist/', FriendMonthList.as_view(), name='monthlist'),
    path('weeklist/', FriendWeekList.as_view(), name='weeklist'),
    path('listall/', friends_listall, name = 'listall'),
    path('todaylist', FriendTodayList.as_view(), name='todaylist'),
    path('create/', FriendCreate.as_view(), name='create'),
    path('delete/<int:pk>', FriendDelete.as_view(), name='delete'),
    path('update/<int:pk>', FriendUpdate.as_view(), name='update'),
    path('detail1/<int:pk>', FriendDetail1.as_view(), name='detail1'),
    path('detail/<int:pk>', FriendDetail.as_view(), name='detail'),
    path('connect/<int:pk>', FriendConnect, name='friendConnect'),
    path('', Main.as_view(), name='main')
]