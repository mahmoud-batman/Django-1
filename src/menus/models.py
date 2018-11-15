# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from restaurants.models import Restaurant

class Item(models.Model):
    user        = models.ForeignKey(User)
    restaurant  = models.ForeignKey(Restaurant)
    name        = models.CharField(max_length= 130)
    contents    = models.TextField(help_text = "Separate Items by comma !")
    excludes    = models.TextField(help_text = "Separate Items by comma !" , null=True , blank=True )
    public      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add = True)
    updated     = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta :
        ordering = ["-updated"]

    def get_absolute_url(self):
        return reverse("menus:details" , kwargs={"pk" : self.pk})

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")
