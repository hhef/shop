from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"
