from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('product/<id>/',views.product,name="products"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('glass_surface/<id>/',views.glass_surface,name="glass_surface")
]
