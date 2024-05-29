from django.urls import path

from calcApp import views

urlpatterns = [
    path('',views.home),
    path('display',views.display),
]