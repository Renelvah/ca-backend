from django.conf.urls import url, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('albumPattern', AlbumPatternViewset, basename='albumPattern')
router.register('theme', ThemeViewset, basename='theme')
router.register('albumLayout', AlbumLayoutViewset, basename='albumLayout')
router.register('albumType', AlbumTypeViewset, basename='albumType')
router.register('size', SizeViewset, basename='size')
router.register('order', OrderViewset, basename='order')
router.register('review', ReviewViewset, basename='review')

urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
