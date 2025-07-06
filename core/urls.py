from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

core = DefaultRouter()
core.register(r'books', BookViewSet, basename='book')

urlpatterns = core.urls  # ✅ Not wrapped in a list
