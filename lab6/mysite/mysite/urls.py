"""
URL configuration for mysite project.

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
from rest_framework.authtoken.views import obtain_auth_token
from app_www.views import OsobaListCreate, OsobaDetail, StanowiskoListCreate, StanowiskoDetail, OsobaUpdateView, OsobaDeleteView, StanowiskoMembersView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/osoba/', OsobaListCreate.as_view(), name='osoba-list-create'),
    path('api/osoba/<int:pk>/', OsobaDetail.as_view(), name='osoba-detail'),
    path('api/osoba/', OsobaListCreate.as_view(), name='osoba-list-create'),
    path('api/osoba/<int:pk>/update/', OsobaUpdateView.as_view(), name='osoba-update'),
    path('api/osoba/<int:pk>/delete/', OsobaDeleteView.as_view(), name='osoba-delete'),
    path('api/stanowisko/', StanowiskoListCreate.as_view(), name='stanowisko-list-create'),
    path('api/stanowisko/<int:pk>/', StanowiskoDetail.as_view(), name='stanowisko-detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('stanowisko/<int:pk>/members/', StanowiskoMembersView.as_view(), name='stanowisko-members'),
]


