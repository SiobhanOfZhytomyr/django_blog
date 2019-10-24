from django import forms
from .models import Post



class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'thumbnail','slug', 'keywords')