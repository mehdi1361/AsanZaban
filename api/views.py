# from django.shortcuts import render
# from rest_framework import viewsets,authtoken,permissions,authentication
# from training.models import Provider, Category
# from training.serializers import ProviderSerializer, CategorySerializer
# from rest_framework import serializers
# # Create your views here.
#
#
# class DefaultsMixin(object):
#     """Default settings for view authentication, permissions,
#     filtering and pagination."""
#     # authentication_classes = (
#     #     authentication.BasicAuthentication,
#     #     authentication.TokenAuthentication,
#     # )
#     # permission_classes = (
#     #     permissions.IsAuthenticated,
#     # )
#     paginate_by = 25
#     max_paginate_by = 100
#
# class ProviderViewSet(DefaultsMixin, viewsets.ModelViewSet):
#
#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer
#
#
# class CategoryViewSet(DefaultsMixin,viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
