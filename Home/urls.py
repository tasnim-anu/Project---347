from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('about', views.about, name='About'),
    path('contact', views.contact, name='Contact'),
    path('review', views.review, name='Review'),
    path('cart', views.cart, name='cart'),
    path('category/<str:category>/', views.category_products, name='category_products'),
    path('search/', views.search_products, name='search_products'),
    path('products/', views.product_list, name='product_list'),

]
