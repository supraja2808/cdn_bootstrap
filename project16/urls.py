"""
URL configuration for project16 project.

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
from django.urls import path
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cdn_bootstrap/',cdn_bootstrap,name='cdn_bootstrap'),
    path('badges/',badges,name='badges'),
    path('breadcrumb/',breadcrumb,name='breadcrumb'),
     path('buttons/',buttons,name='buttons'),
     path('button_group/',button_group,name='button_group'),
     path('card/',card,name='card'),
     path('carousel/',carousel,name='carousel'),
     path('collapse/',collapse,name='collapse'),
     path('dropdowns/',dropdowns,name='dropdowns'),
     path('forms/',forms,name='forms'),
     path('input_group/',input_group,name='input_group'),
      path('jumbortan/',jumbortan,name='jumbortan'),
      path('list_group/',list_group,name='list_group'),
]




