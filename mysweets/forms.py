from django import forms

class SearchForm(forms.Form):
    search=forms.CharField(label='検索(名前)',max_length=80)

