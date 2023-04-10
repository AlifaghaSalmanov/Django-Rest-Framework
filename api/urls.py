from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("api/", views.ProductListAV.as_view(), name="api"),
    path("api/<int:pk>/", views.ProductDetailAV.as_view(), name="api_detail"),
    path("api/<int:pk>/image", views.ProductCreateImage.as_view(), name="api_image"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
