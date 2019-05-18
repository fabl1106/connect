from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_contents',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment_contents'].label = " 소중한 사람의 이야기를 담아주세요!   "
        self.fields['comment_contents'].widget = forms.TextInput()