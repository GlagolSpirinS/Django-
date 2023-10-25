
from django.contrib import admin
from django.urls import path
from django.urls import include

from praktosik_app import views as v, views

urlpatterns = [
    path('', views.index, name='main'),
    path('reviev/', views.send, name='reviev'),
    path('people_search/', views.poisk, name='people_seacrh'),
    path('item_search/', views.item_search, name='item_search'),
    path('product/', views.product_form, name='ProductForm')
]