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

from django.urls import path
from berita.views import (
  dashboard, 
  kategori_list, 
  kategori_add, 
  kategori_update, 
  kategori_delete, 
  artikel_list,
  artikel_add,
  artikel_detail,
  artikel_update,
  artikel_delete

)
urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('/kategori/list', kategori_list, name='kategori_list'),
    path('/kategori/add', kategori_add, name='kategori_add'),
    path('/kategori/update/<int:id_kategori>', kategori_update, name="kategori_update"),
    path('/kategori/delete/<int:id_kategori>', kategori_delete, name="kategori_delete"),
    
   path('/artikel/list', artikel_list, name='artikel_list'),
   path('/artikel/add', artikel_add, name='artikel_add'),
   path('/artikel/detail<int:id_artikel>', artikel_detail, name="artikel_detail"),
   path('/artikel/update<int:id_artikel>', artikel_update, name="artikel_update"),
   path('/artikel/delete<int:id_artikel>', artikel_delete, name="artikel_delete")
]

