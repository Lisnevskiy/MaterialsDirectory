from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, MaterialViewSet

router = DefaultRouter()
router.register(r"materials", MaterialViewSet, basename="materials")
router.register(r"categories", CategoryViewSet, basename="categories")

urlpatterns = [
    path("", include(router.urls)),
]
