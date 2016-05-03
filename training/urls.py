from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'provider',views.ProviderViewSet)
router.register(r'category',views.CategoryViewSet)
router.register(r'package',views.PackageViewSet)
router.register(r'lesson',views.LessonViewSet)
