"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home_page, contact_page, login_page, register_page
from django.conf import settings
from django.conf.urls.static import static
from products.views import ProductListView, ProductDetailView, ProductDetailSlugView

urlpatterns = [
    path("", home_page),
    path("contact/", contact_page, name="contact"),
    path("login/", login_page, name='login'),
    path("register/", register_page, name='register'),
    path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view(), name='products'),
    # path('products/<int:pk>/', ProductDetailView.as_view()),
    path('products/<slug:slug>/', ProductDetailSlugView.as_view(), name='product-detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
