from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    category_new = forms.CharField(required = False, max_length= 150, label = 'New Category')
    class Meta:
        model = Post
        fields = ['recipe', 'category', 'desc', 'image']

    