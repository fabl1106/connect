from django.contrib.auth.models import User
from django import forms

class SignUpForm(forms.ModelForm):

    password = forms.CharField(label = 'Password', widget=forms.PasswordInput)
    Repeat_password = forms.CharField(label = 'Repeat_password', widget=forms.PasswordInput )
    phone = forms.CharField(label='phone', max_length=13)

    class Meta:
        model = User
        fields = [ 'username', 'password', 'Repeat_password', 'phone','email', ]

    def clean_Repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['Repeat_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return cd['Repeat_password']