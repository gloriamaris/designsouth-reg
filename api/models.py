# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 200)
    school = models.CharField(max_length = 300)
    email = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)

def __str__(self):
    return '%s %s %s' % (self.name, self.school, self.email)
