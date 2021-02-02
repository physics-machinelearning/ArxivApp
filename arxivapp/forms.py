from django.forms import ModelForm
from django import forms

from .models import Post


YEAR_CHOICES = tuple(
    [(i+2010, i+2010) for i in range(12)]
)

class ArticleSearchForm(forms.Form):
    keyword = forms.CharField(
        label='Keyword', max_length=100, required=False
    )
    start_year = forms.ChoiceField(
        label='From',
        widget=forms.Select,
        choices=YEAR_CHOICES,
        required=False
    )
    end_year = forms.ChoiceField(
        label='To',
        widget=forms.Select,
        choices=YEAR_CHOICES,
        required=False
    )
    author = forms.CharField(
        label='Author', max_length=100, required=False
    )


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['article'].widget = forms.HiddenInput()
        self.fields['user'].widget = forms.HiddenInput()

    class Meta:
        model = Post
        fields = ('content', 'article', 'user')
        labels = {
            'content': 'comment'
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows':4, 'cols':80}),
        }

