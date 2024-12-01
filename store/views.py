from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.http import HttpResponse
from .forms import ProductForm, CategoryForm  # Ensure these forms exist in forms.py

# User Signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after signup
    else:
        form = UserCreationForm()
    # Correct template path to match your directory structure
    return render(request, 'registration/signup.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    # Correct template path to match your directory structure
    return render(request, 'registration/login.html', {'form': form})

# User Logout
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to the login page after logout


# Home View
@login_required
def home(request):
    categories = Category.objects.all()
    is_admin = request.user.is_staff  # Identify admin users
    return render(request, 'home.html', {'categories': categories, 'is_admin': is_admin})

# Product List
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

# About Page
def about(request):
    return render(request, 'about.html')

# Contact Page
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse("Thank you for reaching out!")
    return render(request, 'contact.html')

# Category List
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

# Admin Dashboard with CRUD operations
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'admin_dashboard.html', {'products': products, 'categories': categories})

# Create, Update, and Delete Product (Admin Only)
@user_passes_test(lambda u: u.is_staff)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm()
    return render(request, 'admin/product_form.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'admin/product_form.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_dashboard')
    return render(request, 'admin/product_confirm_delete.html', {'product': product})
