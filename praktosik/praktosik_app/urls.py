
from django.contrib import admin
from django.urls import path
from django.urls import include

from praktosik_app import views as v, views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviev/', views.reviev, name='reviev')
]