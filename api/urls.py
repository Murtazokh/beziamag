from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]