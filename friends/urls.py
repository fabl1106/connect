from django.urls import path

from friends.models import Friends
from .views import FriendCreate, FriendDelete, FriendDetail, FriendList, FriendUpdate, FriendDetail1, FriendConnect, \
    comment_write, friends_listall, FriendWeekList, FriendMonthList


app_name = 'friend'
urlpatterns = [
    path('detail/comment/<int:pk>/', comment_write, name='comment'),
    path('monthlist/', FriendMonthList.as_view(), name='monthlist'),
    path('weeklist/', FriendWeekList.as_view(), name='weeklist'),
    path('listall/', friends_listall, name = 'listall'),
    path('create/', FriendCreate.as_view(), name='create'),
    path('delete/<int:pk>', FriendDelete.as_view(), name='delete'),
    path('update/<int:pk>', FriendUpdate.as_view(), name='update'),
    path('detail1/<int:pk>', FriendDetail1.as_view(), name='detail1'),
    path('detail/<int:pk>', FriendDetail.as_view(), name='detail'),
    path('connect/<int:pk>', FriendConnect, name='friendConnect'),
    path('', FriendList.as_view(), name='index'),
]