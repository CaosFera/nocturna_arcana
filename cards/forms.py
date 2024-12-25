from django import forms




class Searchform(forms.Form):
    query = forms.CharField()