# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
import random

# Create your models here.
class Restaurant(models.Model):
    owner       = models.ForeignKey(User)
    name        = models.CharField(max_length= 130)
    location    = models.CharField(max_length= 130 , null=True , blank=True )
    category    = models.CharField(max_length= 130 , null=True , blank=True )
    timestamp   = models.DateTimeField(auto_now_add = True)
    updated     = models.DateTimeField(auto_now = True)
    slug        = models.SlugField(unique=True, null=True , blank=True) # hide from admin

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("restaurants:details" , kwargs={"slug" : self.slug})

    class Meta:
        ordering = ["-updated"]
        permissions = (
        ("can_read", 'can read seko seko'),
        )

def pre_save_reciever(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug  = slugify(instance.name)+'-'+str(random.randint(1,1000000000))

pre_save.connect(pre_save_reciever, Restaurant)
