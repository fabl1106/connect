from django.urls import path
from .views import FriendCreate, FriendDelete, FriendDetail, FriendList, FriendUpdate
from friends import views


app_name = 'friend'
urlpatterns = [
    path('detail/comment/<int:pk>/', views.comment_write, name='comment'),
    path('create/', FriendCreate.as_view(), name='create'),
    path('delete/<int:pk>', FriendDelete.as_view(), name='delete'),
    path('update/<int:pk>', FriendUpdate.as_view(), name='update'),
    path('detail/<int:pk>', FriendDetail.as_view(), name='detail'),
    path('', FriendList.as_view(), name='index'),
]