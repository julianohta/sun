# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.urls import reverse_lazy
from models import Page, SimplePage
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain


# Create your views here.
def list_view(request, page=1, article_genre='current_events'):

    def switch(x):
        try:
            return {
                'current_events': 'CE',
                'opinion': 'OP',
                'sports': 'SP',
                'entertainment': 'ET',
                'science': 'SC',
                'dining': 'DN'
            }[x]
        except KeyError:
            return None

    genre_query = switch(article_genre)

    if not genre_query:
        return redirect(reverse_lazy('pages:page_list', kwargs={'page': 1, 'article_genre': 'current_events'}))

    # queryset = Page.objects.filter(genre=genre_query)
    queryset = list(chain(SimplePage.objects.filter(genre=genre_query), Page.objects.filter(genre=genre_query)))

    page_list = queryset
    paginator = Paginator(page_list, 25)  # Show 25 contacts per page

    try:
        featured = Page.objects.get(featured=True)
    except Page.DoesNotExist:
        featured = None

    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pages = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pages = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'pages': pages, 'genre': article_genre, 'featured': featured, })
    # 'filter': article_filter


def detail_view(request, slug):
    try:
        page = Page.objects.get(slug=slug)
        return render(request, 'detail.html', {'page': page})
    except Page.DoesNotExist:
        page = SimplePage.objects.get(slug=slug)
        if not page.alt:
            return render(request, 'simple_detail.html', {'page': page})
        else:
            return render(request, 'simple_detail2.html', {'page': page})

