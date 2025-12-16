from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('login/', auth_views.LoginView.as_view(template_name='Home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup, name='signup'),
]

