# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Page(models.Model):

    CURRENT_EVENTS = 'CE'
    OPINION = 'OP'
    SPORTS = 'SP'
    ENTERTAINMENT = 'ET'
    SCIENCE = 'SC'
    DINING = 'DN'

    GENRES = (
        (CURRENT_EVENTS, 'Current Events'),
        (OPINION, 'Opinion'),
        (SPORTS, 'Sports'),
        (ENTERTAINMENT, 'Entertainment'),
        (SCIENCE, 'Science'),
        (DINING, 'Dining'),
    )

    genre = models.CharField(max_length=2, choices=GENRES, default=CURRENT_EVENTS)
    title = models.CharField(null=True, max_length=50)
    date = models.DateTimeField(auto_now=True, null=True)
    img = models.ImageField(upload_to='%Y/%m/%d', null=True)
    css = models.FileField(upload_to='file_uploads/')
    html = RichTextUploadingField()
    head = models.TextField(null=True)
    slug = models.CharField(max_length=20)
    summary = models.CharField(max_length=200, null=True)
    visible = models.BooleanField(default=False)
    author = models.CharField(max_length=100, null=True)
