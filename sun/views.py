# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render
from itertools import chain
from pages.models import Page, SimplePage, ProjectPage
from django.shortcuts import render_to_response


def sun_redirect(request):
    return redirect("http://cornellsun.com/")


def list_view(request):
    # get all page, simple page, project page
    # check if any featured
    # remove featured and add to context
    # rest added as pages

    p1 = Page.objects.filter(visible=True, featured=True)
    p2 = SimplePage.objects.filter(visible=True, featured=True)
    p3 = ProjectPage.objects.filter(visible=True, featured=True)

    if not p1:
        if not p2:
            featured = p3
        else:
            featured = p2
    else:
        featured = p1

    featured_slug = featured.first().slug

    print("SLUG: {}".format(featured_slug))

    pages = list(chain(Page.objects.filter(visible=True).exclude(slug=featured_slug),
                       SimplePage.objects.filter(visible=True).exclude(slug=featured_slug),
                       ProjectPage.objects.filter(visible=True).exclude(slug=featured_slug)))

    first = pages[0]

    triplet = []
    while len(pages) > 0:
        triple = pages[:3]
        triplet.append(triple)
        pages = pages[3:]

    return render(request, 'list.html', context={'first': featured.first(), 'triplet': triplet, })


def contact_view(request):
    return render(request, 'contact.html', context={})

