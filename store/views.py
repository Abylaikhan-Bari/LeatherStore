from django.shortcuts import render
from .models import Category, Product

def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})
