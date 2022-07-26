from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='Title:',
        widget=forms.TextInput(attrs={"placeholder": "Your title"})
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write some article",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 120
            }
        )
    )
    active = forms.BooleanField()
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]
