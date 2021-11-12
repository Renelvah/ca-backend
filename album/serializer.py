from .models import *
from rest_framework import serializers


class AlbumPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPattern
        fields = ['id', 'title', 'theme', 'photo']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'size']


class AlbumLayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumLayout
        fields = ['id', 'type', 'size', 'minPages']


class AlbumTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumType
        fields = ['id', 'type']


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id', 'theme', 'description']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name', 'email', 'albumPattern', 'albumLayout', 'pagesCount', 'date', 'description', 'status']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'email', 'date', 'rate', 'text']
