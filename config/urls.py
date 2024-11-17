from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("materials.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),  # JSON-схема
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),  # Swagger UI
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),  # Redoc UI
]
