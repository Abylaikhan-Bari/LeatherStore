from django.shortcuts import render
from .models import Product, Category


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Save or process the data (e.g., send email)
    return render(request, 'contact.html')

def category_list(request):
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'categories.html', {'categories': categories})