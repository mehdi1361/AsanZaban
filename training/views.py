
from django.shortcuts import render
from rest_framework.decorators import detail_route, api_view
from rest_framework.views import APIView
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


# class HomeViewSet(DefaultsMixin, viewsets.ViewSet):
#     def list(self, request):
#         return Response({'id':'200','message':'ok'})
#     @detail_route(methods=['post'])
#     def fetch_data(self, request):
#         return Response({'id':'200','message':'ok'})

# class HomeView(APIView):
#     def get_object(self):
#         try:
#             return Response({'id':'200','message':'ok'})
#         except :
#             return Response({'id':'400','message':'error'})

@api_view(['GET'])
def home(request, pk):
    try:
        selectde_user = User.objects.get(pk=pk)
        main_dict = {}
        my_account = {"id": selectde_user.id, "name":selectde_user.name}
        main_dict["my_account"]=my_account
        main_dict["my_package"] = user_package(selectde_user)
        main_dict["suggested_package"] = suggested_packages(selectde_user)
        main_dict["category"] = Category.category_tree()
        return Response(main_dict)

    except User.DoesNotExist:
        return Response({'id':'400','message':'cant find pk'})

def user_package(user):
    user_packages = UserPackage.objects.filter(user=user)
    packages = []
    for i in user_packages:
        packages.append({"id": i.package.id, "name":i.package.name,
                         "price": i.package.price,"discount": i.package.discount,
                         "photo": str(i.package.photo), "archive": i.is_archive})
    return packages

def suggested_packages(user):
    packages = []
    suggested_package = Package.objects.all().exclude(userpackage__user=user)
    for i in suggested_package:
        packages.append({"id": i.id, "name": i.name,"price": i.price,"discount": i.discount,"photo": str(i.photo)})

    return packages



    # home_profile = User.objects.get(pk=send_user)
    # user_package = UserPackage.objects.filter(user=send_user)
    # category = Category.category_tree(request)
    # return Response({'id':'200','message':'ok'})
#
# @api_view(['GET'])
# def get_categories(request,parent_id=None):
#     return Response(Category.category_tree(request, parent_id))
