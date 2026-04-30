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