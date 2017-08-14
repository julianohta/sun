# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import Page
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def list_view(request, page=1):
    page_list = Page.objects.all()
    paginator = Paginator(page_list, 25)  # Show 25 contacts per page

    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pages = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pages = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'pages': pages})


def detail_view(request, slug):
    page = Page.objects.get(slug=slug)
    return render(request, 'detail.html', {'page': page})
