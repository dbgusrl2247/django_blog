from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["category", "title", "content"]
        widgets = {
            "category": forms.Select(attrs={"class": "form-select"}),
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "제목"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 10, "placeholder": "내용"}),
        }
