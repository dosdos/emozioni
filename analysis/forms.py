# -*- coding: utf-8 -*-
from django import forms

from .models import Search


class SearchForm(forms.ModelForm):
    query = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Scrivi qui la tua frase!"}))

    class Meta:
        model = Search
        fields = ('query', )
