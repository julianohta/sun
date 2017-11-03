# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import SnapCode


# Create your views here.
def snap_view(request):

    return render(request, 'snap.html', context={'snap_obj':  SnapCode.objects.latest('date'), })
