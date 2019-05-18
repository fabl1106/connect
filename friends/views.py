from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views.generic.base import View, TemplateResponseMixin
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from friends.forms import CommentForm
from .models import Friends, Comment
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
import math
from datetime import date, datetime, timedelta



class FriendList(ListView):
    model = Friends
    template_name_suffix = "_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Friends.objects.filter(scheduled_connect__lte=date.today())
        return context


class FriendWeekList(ListView):
    model = Friends
    template_name_suffix = "_weeklist"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Friends.objects.filter(scheduled_connect__lte=date.today(), scheduled_connect__gte=date.today()-timedelta(days=7))
        return context


class FriendMonthList(ListView):
    model = Friends
    template_name_suffix = "_monthlist"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Friends.objects.filter(scheduled_connect__lte=date.today(), scheduled_connect__gte=date.today()-timedelta(days=30))
        return context


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
    template_name = 'friends/friends_detail.html'


    def dispatch(self, request, *args, **kwargs):
        #url에서 설정해준 주소로 바든ㄴ다.
        friend_id = kwargs['pk']
        friend = get_object_or_404(Friends, pk=friend_id)

        if request.method == "POST":
            comment_contents = request.POST.get('comment_contents')
            Comment.objects.create(friend=friend, comment_contents=comment_contents)

        comment = friend.friend.all()
        comment_form = CommentForm()
        return render(request, "friends/friends_detail.html", {'Comment': comment, 'object': friend, 'form': comment_form})

    #
    # def get(self, request, *args, **kwargs):
    #     friend_id = kwargs['friend_id']
    #     print("f_id : {}".format(friend_id))
    #     friend = get_object_or_404(Friends, pk=friend_id)
    #     print("friend : {}".format(friend))
    #     comment = friend.comment.all()
    #     print("comment : {}".format(comment))
    #
    #
    # def post(self, request, *args, **kwargs):
    #     friend_id = kwargs['friend_id']
    #     friend = get_object_or_404(Friends, pk = friend_id)
    #     comment_contents = request.POST.get('comment')
    #
    #     if not comment_contents:
    #         messages.info(request, "You don't write anything...")
    #         return HttpResponseRedirect(reverse_lazy('friend:detail', args=[friend_id]))
    #         Comment.objects.create(friend=friend, comment_contents=comment_contents)
    #
    #     comment = Comment.objects.all()
    #     return render(request, "friends/friends_detail.html", {'Comment': comment, 'object': friend})


class FriendDetail1(DetailView):
    model = Friends
    template_name = 'friends/friends_detail1.html'

    # def get(self, request, pk,):
    #     comment = Comment.objects.all()
    #     context_data = self.get_context_data()
    #     context_data['Comment'] = Comment.objects.all()
    #     friend = Friends.objects.get(id=pk)
    #     return render(request, self.template_name, context_data)

    # 데이터만 넘겨받는 방법이다.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Comment'] = context['object'].friend.all()
        return context

    # def get(self, request, pk,):
    #     comment = Comment.objects.all()
    #     friend = Friends.objects.get(id=pk)
    #     return render(request, self.template_name, {"Comment":comment, "object":friend})

def FriendConnect(request, pk):
    model = Friends
    return model.updateconnect(request, pk)


# class FriendComment(CreateView):
#     model = Comment
#     fields = ['comment_contents']
#     template_name = 'friends/friends_comment.html'
#
#     def form_valid(self, form):
#         form.instance.friend_id = Friends.id
#         if form.is_valid():
#             form.instance.save()
#             return redirect('/')
#         else:
#
#             return self.render_to_response({'form': form})


def comment_write(request, pk):
    if request.method == "POST":
        friend = get_object_or_404(Friends, id=pk)
        comment_contents = request.POST.get('comment')
        print(friend)
        if not comment_contents:
            messages.info(request, "You don't write anything...")
            return HttpResponseRedirect(reverse_lazy('friend:detail', args=[pk]))
        else:
            Comment.objects.create(friend=friend, comment_contents=comment_contents)
        comment = Comment.objects.all()
    return render(request,"friends/friends_detail1.html", {'Comment':comment,'object':friend})

#여기서는 리다이렉트만 시켜주고 db는 detail1에서 띄어주도록 한다.
# 그냥 단순히 friends_detail로 이동하게 되니 , 있어야 할 값들이 없어서 그렇다.(generic view이기 때문에 알아서 생성해주는 값들이 없어서 ㄱ

def friends_listall(request):

    page = int(request.GET.get('page', 1))

    paginated_by = 10

    search_key = request.GET.get('search_key', None)
    friend_name_q = Q(friend_name__icontains=search_key)
    friend_mobile_q = Q(friend_mobile__icontains=search_key)
    friend_memo_q = Q(friend_memo__icontains=search_key)

    if search_key:
        # documents = Document.objects.filter(title_q | text_q)
        Friends_list = get_list_or_404(Friends, friend_name_q | friend_mobile_q | friend_memo_q)
    else:
        # documents = get_list_or_404(Document,title__contains="1")
        Friends_list = get_list_or_404(Friends)

    total_count = len(Friends_list)
    total_page = math.ceil(total_count / paginated_by)
    page_range = range(1, total_page + 1)
    start_index = paginated_by * (page - 1)
    end_index = paginated_by * page

    Friends_list = Friends_list[start_index:end_index]

    return render(request, 'friends/friends_listall.html',
                  {'Friends_list': Friends_list, 'total_page': total_page, 'page_range': page_range})
