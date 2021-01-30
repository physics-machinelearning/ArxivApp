from django import forms

YEAR_CHOICES = tuple(
    [i+2010 for i in range(12)]
)

class ArticleSearchForm(forms.Form):
    keyword = forms.CharField(
        label='keyword', max_length=100, required=False
    )
    start_year = forms.ChoiceField(
        label='year',
        widget=forms.Select,
        choices=YEAR_CHOICES,
        requred=False
    )
    end_year = forms.ChoiceField(
        label='year',
        widget=forms.Select,
        choices=YEAR_CHOICES,
        requred=False
    )
    author = = forms.CharField(
        label='keyword', max_length=100, required=False
    )
