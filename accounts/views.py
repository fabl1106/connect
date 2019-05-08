from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from accounts import *

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        # todo : 입력 받은 내용을 이용해서 회원 객체 생성
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            user_instance = signup_form.save(commit=False)
            user_instance.set_password(signup_form.cleaned_data['password'])
            user_instance.save()
            return render(request, 'accounts/signup_complete.html', {'username':user_instance.username})

    else:
        # todo: from 객체를 만들어서 전달.
        signup_form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': signup_form.as_p() })