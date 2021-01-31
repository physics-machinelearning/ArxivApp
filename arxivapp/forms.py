from django import forms

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
