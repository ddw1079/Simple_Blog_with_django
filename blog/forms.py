from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = { 'title', 'text'}
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'id': '',
                'style': "",
                'placeholder': "title"
            }),
            'text': forms.Textarea(attrs={
                'class': "form-control",
                'id': 'article_input',
                'style': "",
                "placeholder": "text"
            }),
        }
        