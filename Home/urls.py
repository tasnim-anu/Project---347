from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('about', views.about, name='About'),
    path('contact', views.contact, name='Contact'),
    path('review', views.review, name='Review'),
    path('product', views.product, name='product'),
    path('cart', views.cart, name='cart'),
]
