from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('product',views.product,name="product"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('glass_surface/<id>/',views.glass_surface,name="glass_surface")
]
