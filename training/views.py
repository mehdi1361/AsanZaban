
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets,authtoken,permissions,authentication
from .models import Provider, Category, Package, Lesson, User, UserPackage
from .serializers import ProviderSerializer, CategorySerializer, PackageSerializer, LessonSerializer
from rest_framework import serializers
# Create your views here.


class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""
    # authentication_classes = (
    #     authentication.BasicAuthentication,
    #     authentication.TokenAuthentication,
    # )
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    paginate_by = 25
    max_paginate_by = 100

class ProviderViewSet(DefaultsMixin, viewsets.ModelViewSet):

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class CategoryViewSet(DefaultsMixin,viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PackageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class LessonViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer



@api_view(['GET'])
def home(request):
    send_user = request.data['user']
    home_profile = User.objects.get(pk=send_user)
    user_package = UserPackage.objects.filter(user=send_user)
    category = Category.objects.all()
