from django import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('praktosik_app/', include('praktosik_app.urls')),
]
