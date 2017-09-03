# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.urls import reverse_lazy


def list_redirect(request):
    return redirect(reverse_lazy('pages:page_list', kwargs={'page': 1, 'article_genre': 'current_events'}))
