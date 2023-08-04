from django.contrib import admin
from django.urls import path
from cal_app import views

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('calculate',views.calculate,name="calculate"),
]
