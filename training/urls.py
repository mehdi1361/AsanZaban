from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'provider',views.ProviderViewSet)
router.register(r'category',views.CategoryViewSet)
router.register(r'package',views.PackageViewSet)
router.register(r'lesson',views.LessonViewSet)
# router.register(r'home', views.HomeViewSet , base_name='supplier-projects')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^home/(?P<pk>\d+)/$', views.home),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
