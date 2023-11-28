from django import forms

class MusicSearchForm(forms.Form):
    search_query = forms.CharField(required=False, label='Search Music')