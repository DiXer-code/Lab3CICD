from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'menu/index.html')

def menu_page(request):
    # Пізніше сюди додамо отримання страв з бази даних
    return render(request, 'menu/menu.html')

def about(request):
    return render(request, 'menu/about.html')

def book(request):
    return render(request, 'menu/book.html')

def health_check(request):
    # A small operational endpoint lets Docker and CI verify that Django starts correctly.
    return JsonResponse({"status": "ok", "service": "restaurant-menu"})
