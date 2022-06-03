from django.contrib import admin
from django.urls import path

from detection import views

urlpatterns = [
    path('', views.home, name='index'),
    path('facecam_feed', views.facecam_feed, name='facecam_feed'),
]
