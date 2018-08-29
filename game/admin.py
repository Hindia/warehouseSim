# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Shelf, Compartment, Item

# Register your models here.
admin.site.register(Shelf)
admin.site.register(Compartment)
admin.site.register(Item)