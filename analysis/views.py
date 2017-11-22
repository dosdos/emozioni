# -*- coding: utf-8 -*-
from django.shortcuts import render

from analysis.services import get_nlp_analysis, get_sentences
from .forms import SearchForm


# from django.contrib.auth.decorators import login_required
# @login_required(login_url='/admin/login/')
def home(request, template_name="home.html"):
    form = SearchForm()
    analysis = {}

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            if request.user.is_authenticated():
                search.user = request.user
            search.nlp_analysis = get_nlp_analysis(form.cleaned_data.get('query'))
            search.save()
            analysis = get_sentences(search.nlp_analysis)

    return render(request, template_name, {
        'form': form,
        'analysis': analysis,
    })
