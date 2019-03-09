# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Shelf, Compartment, Item
from .serializers import ShelfSerializer, CompartmentSerializer, ItemSerializer


# Create your views here.
def game(request):
    return render(request, 'game/game.html')


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


class ShelfList(APIView):

    def get(self, request):
        shelves = Shelf.objects.all()
        serializer = ShelfSerializer(shelves, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class CompartmentList(APIView):

    def get(self, request):
        compartments = Compartment.objects.all()
        serializer = CompartmentSerializer(compartments, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class ItemList(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self):
        pass