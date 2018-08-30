# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render
from .models import Shelf, Compartment, Item


# Create your views here.
def index(request):
    all_shelves = Shelf.objects.all()
    return render(request, 'game/index.html', {'all_shelves': all_shelves})


def detail(request, shelfNum):
    try:
        shelf = Shelf.objects.get(pk=shelfNum)
    except Shelf.DoesNotExist:
        raise Http404("Shelf doesnt exist")
    return render(request, 'game/detail.html', {'shelf': shelf})


def moredetail(request, shelfNum, compartmentNum):
        compartment = Compartment.objects.get(pk=compartmentNum)
        shelf = Shelf.objects.get(pk=shelfNum)
        return render(request, 'game/moredetail.html', {'compartment': compartment, 'shelf': shelf})