# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Page, SimplePage, ProjectPage


def make_visible(modeladmin, request, queryset):
    queryset.update(visible=True)
make_visible.short_description = "Mark selected stories as visible"


def make_invisible(modeladmin, request, queryset):
    queryset.update(visible=False)
make_invisible.short_description = "Mark selected stories as invisible"


def make_featured(modeladmin, request, queryset):
    queryset.update(featured=True)
make_featured.short_description = "Mark selected stories as featured"


def make_unfeatured(modeladmin, request, queryset):
    queryset.update(featured=False)
make_unfeatured.short_description = "Mark selected stories as unfeatured"


class SimplePageAdmin(admin.ModelAdmin):
    list_display = ['title', 'visible', 'featured']
    actions = [make_visible, make_invisible, make_featured, make_unfeatured]


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'visible', 'featured']
    actions = [make_visible, make_invisible, make_featured, make_unfeatured]


class ProjectPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'visible', 'featured']
    actions = [make_visible, make_invisible, make_featured, make_unfeatured]

# Register your models here.
admin.site.register(Page, PageAdmin)
admin.site.register(SimplePage, SimplePageAdmin)
admin.site.register(ProjectPage, ProjectPageAdmin)
