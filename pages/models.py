# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Page(models.Model):
    title = models.CharField(null=True, max_length=50)
    date = models.DateTimeField(auto_now=True, null=True)
    img = models.ImageField(upload_to='%Y/%m/%d', null=True)
    css = models.FileField(upload_to='uploads/')
    html = models.TextField()
    head = models.TextField(null=True)
    slug = models.CharField(max_length=20)
    visible = models.BooleanField(default=False)
