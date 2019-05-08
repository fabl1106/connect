from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Friends, Comment
from django.contrib import messages
from django.urls import reverse_lazy

class FriendList(ListView):
    model = Friends


class FriendCreate(CreateView):
    model = Friends
    fields = ['user', 'friend_name', 'friend_mobile', 'friend_group', 'friend_relation', 'friend_memo' ]
    template_name_suffix = '_create'
    success_url = '/'


class FriendUpdate(UpdateView):
    model = Friends
    fields = ['user', 'friend_name', 'friend_mobile', 'friend_group', 'friend_relation', 'friend_memo']
    template_name_suffix = '_update'
    success_url = '/'


class FriendDelete(DeleteView):
    model = Friends
    template_name_suffix = '_delete'
    success_url = '/'


class FriendDetail(DetailView):
    model = Friends
    template_name_suffix = '_detail'


@login_required
def comment_write(request, pk):
    model = Comment
    if request.method == "POST":
        post = get_object_or_404(Friends, id=pk)
        content = request.POST.get('content')

        conn_user = request.user

        if not content:
            messages.info(request, "You don't write anything...")
            return HttpResponseRedirect(reverse_lazy('friend:detail'))
        else:
            Comment.objects.create(post=post, comment_writer = conn_user, comment_contents = content)
        return HttpResponseRedirect(reverse_lazy('friend:detail', args=[post.id]))
