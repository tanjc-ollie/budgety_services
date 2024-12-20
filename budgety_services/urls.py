"""
URL configuration for budgety_services project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test, name='test'),
    path('api/search_plaid_institutions', views.search_plaid_institutions, name='search_plaid_institutions'),
    path('api/get_plaid_access_token', views.get_plaid_access_token, name='get_plaid_access_token'),
    path('api/get_plaid_link_token', views.get_plaid_link_token, name='get_plaid_link_token'),
    path('api/get_plaid_transactions', views.get_plaid_transactions, name='get_plaid_transactions'),
]
