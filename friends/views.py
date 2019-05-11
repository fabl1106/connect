from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

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
    fields = ['friend_name', 'friend_mobile', 'friend_group', 'friend_relation', 'latest_connect', 'friend_memo' ]
    template_name_suffix = '_create'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        if form.is_valid():
            # 올바르다면
            # form : 모델폼
            form.instance.save()
            return redirect('/')
        else:
            # 올바르지 않다면
            return self.render_to_response({'form': form})



class FriendUpdate(UpdateView):
    model = Friends
    fields = ['friend_name', 'friend_mobile', 'friend_group', 'friend_relation', 'latest_connect', 'friend_memo']
    template_name_suffix = '_update'
    success_url = '/'


class FriendDelete(DeleteView):
    model = Friends
    template_name_suffix = '_delete'
    success_url = '/'


class FriendDetail(DetailView):
    model = Friends
    template_name_suffix = '_detail'


class FriendDetail1(DetailView):
    model = Friends
    template_name_suffix = '_detail1'



def FriendConnect(request, pk):
    model = Friends
    return model.updateconnect(request, pk)


class FriendComment(CreateView):
    model = Comment
    fields = ['comment_contents']
    template_name = 'friends/friends_comment.html'

    def form_valid(self, form):
        form.instance.friend_id = Friends.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            # 올바르지 않다면
            return self.render_to_response({'form': form})


# def comment_write(request, pk):
#     model = Comment
#     fields = ['comment_contents']
#     def form_valid(self, form):
#         form.instance.user_id = self.request.user.id
#         if form.is_valid():
#             # 올바르다면
#             # form : 모델폼
#             form.instance.save()
#             return redirect('/')
#         else:
#             # 올바르지 않다면
#             return self.render_to_response({'form': form})

    # if request.method == "POST":
    #     writer = get_object_or_404(Friends, id=pk)
    #     content = request.POST.get('content')
    #
    #     if not content:
    #         messages.info(request, "You don't write anything...")
    #         return HttpResponseRedirect(reverse_lazy('friend:detail'))
    #     else:
    #         Comment.objects.create(post=writer, comment_contents=content)
    #     return HttpResponseRedirect(reverse_lazy('friend:detail'))
