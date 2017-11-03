# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class SnapCode(models.Model):
    img = models.FileField(upload_to='codes/%Y/%m/%d')
    date = models.DateField(auto_now=True)
