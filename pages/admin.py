# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Page


def make_visible(modeladmin, request, queryset):
    queryset.update(visible=True)
make_visible.short_description = "Mark selected stories as visible"


def make_invisible(modeladmin, request, queryset):
    queryset.update(visible=False)
make_invisible.short_description = "Mark selected stories as invisible"


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'visible']
    actions = [make_visible, make_invisible]

# Register your models here.
admin.site.register(Page, PageAdmin)
