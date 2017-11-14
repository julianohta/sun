# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.urls import reverse_lazy


def sun_redirect(request):
    return redirect("http://cornellsun.com/")
