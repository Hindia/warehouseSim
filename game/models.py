# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Shelf(models.Model):
    shelfNum = models.CharField(unique=True, max_length=10)
    shelfPosition = models.CharField(max_length=6)

    def __str__(self):
        return self.shelfNum + ' - ' + self.shelfPosition


class Compartment(models.Model):
    compartmentNum = models.CharField(unique=True, max_length=10)
    compartmentPosition = models.CharField(max_length=4)
    numberOfItems = models.CharField(max_length=500)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)

    def __str__(self):
        return self.compartmentNum + ' - ' + self.compartmentPosition + ' - ' + self.numberOfItems


class Item(models.Model):
    itemName = models.CharField(unique=True, max_length=250)
    itemPic = models.CharField(max_length=1000)
    compartment = models.ForeignKey(Compartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName
