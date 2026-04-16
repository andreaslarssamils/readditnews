from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Comment, Post


class PostForm(forms.ModelForm):
    """Form for creating and editing posts."""

    class Meta:
        model = Post
        fields = ["title", "content", "image", "url", "category"]
        widgets = {
            "content": SummernoteWidget(),
        }

    def clean_title(self):
        from django.utils.text import slugify

        title = self.cleaned_data["title"]
        slug = slugify(title)
        qs = Post.objects.filter(slug=slug)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                "A post with this title already exists. Please choose a different title."
            )
        return title


class CommentForm(forms.ModelForm):
    """Form for creating and editing comments."""

    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Write a comment..."}
            ),
        }
