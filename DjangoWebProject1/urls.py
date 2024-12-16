"""
Definition of urls for DjangoWebProject1.
"""
# -*- coding: utf-8 -*-

from datetime import datetime
from xml.dom.minidom import Document
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.db import models

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('anketa/', views.anketa, name='anketa'),
    path('registration/', views. registration, name= 'registration'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('videopost/', views.videopost, name='videopost'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('catalog/product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('catalog/<int:category_id>/', views.category_detail, name='category_detail'),
    path('cart/', views.cart, name='cart'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('checkout/', views.checkout, name='checkout'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('manage_orders/', views.manage_orders, name='manage_orders'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
   
   path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизоваться',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
