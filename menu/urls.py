from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu_page, name='menu'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
]