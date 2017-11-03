# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import SnapCode


class SnapCodeAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(SnapCode, SnapCodeAdmin)
