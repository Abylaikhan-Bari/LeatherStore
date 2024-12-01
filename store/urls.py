from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Custom logout
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('categories/', views.category_list, name='category_list'),
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth views
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/product/create/', views.product_create, name='product_create'),
    path('admin/product/update/<int:pk>/', views.product_update, name='product_update'),
    path('admin/product/delete/<int:pk>/', views.product_delete, name='product_delete'),
]
