# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from .views import home


urlpatterns = [
    url(r'^$', home, {'template_name': 'home.html'}, 'home'),
]
