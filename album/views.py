from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .models import *


class AlbumLayoutViewset(viewsets.ModelViewSet):
    serializer_class = AlbumLayoutSerializer

    def get_queryset(self):
        album = AlbumLayout.objects.all()
        return album


class AlbumPatternViewset(viewsets.ModelViewSet):
    serializer_class = AlbumPatternSerializer

    def get_queryset(self):
        album = AlbumPattern.objects.all()
        return album


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order = Order.objects.all()
        return order


class AlbumTypeViewset(viewsets.ModelViewSet):
    serializer_class = AlbumTypeSerializer

    def get_queryset(self):
        album = AlbumType.objects.all()
        return album


class SizeViewset(viewsets.ModelViewSet):
    serializer_class = SizeSerializer

    def get_queryset(self):
        size = Size.objects.all()
        return size



class ThemeViewset(viewsets.ModelViewSet):
    serializer_class = ThemeSerializer

    def get_queryset(self):
        theme = Theme.objects.all()
        return theme


class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        review = Review.objects.all()
        return review
