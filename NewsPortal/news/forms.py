from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    #description = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['id','author', 'title', 'content']