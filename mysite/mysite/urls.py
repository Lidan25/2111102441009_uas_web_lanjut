"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from mysite.views import home, about, detail_artikel, contact

from mysite.authentikasi import akun_login, akun_registrasi, akun_logout

from berita.api import *

urlpatterns = [
  path('admin/', admin.site.urls),

  path('', home, name="home"),
  path('about', about, name="about"),
  path('contact', contact,name='contact'),
  path('artikel/<slug:slug>', detail_artikel, name='detail_artikel'),

  path('dashboard', include("berita.urls")),

  path('api/author/list', api_author_list),
    
    path('api/kategori/list', api_kategori_list),
    path('api/kategori/add', api_kategori_add),
    path('api/kategori/detail<int:id_kategori>', api_kategori_detail),
    
    path('api/artikel/list', api_artikel_list),
     path('api/artikel/add', api_artikel_add),
    path('api/artikel/detail<int:id_artikel>', api_artikel_detail),

  path('authentikasi/login', akun_login, name='akun_login'),
  path('authentikasi/registrasi', akun_registrasi, name='akun_registrasi'),
  path('authentikasi/logout', akun_logout, name="akun_logout"),

  
  path('api-auth/', include('rest_framework.urls')),
  path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
