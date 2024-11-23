"""
URL configuration for api_zaliczanie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_zaliczenie.views import AdminOnlyView, UserOnlyView, BookViewSet, CategoryViewSet, RentalViewSet, BookReservationViewSet, UserRegistrationView,UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'rentals', RentalViewSet, basename='rentals')
router.register(r'reservations', BookReservationViewSet, basename='reservations')
router.register(r'users', UserViewSet, basename='users')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin-view/', AdminOnlyView.as_view(), name='admin_view'),
    path('user-view/', UserOnlyView.as_view(), name='user_view'),
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),


]

