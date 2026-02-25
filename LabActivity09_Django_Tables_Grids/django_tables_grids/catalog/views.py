from django.shortcuts import render
from .models import Product

def product_table(request):
    products = Product.objects.all().order_by("id")
    return render(request, "catalog/product_table.html", {"products": products})

def product_grid(request):
    products = Product.objects.all().order_by("id")
    return render(request, "catalog/product_grid.html", {"products": products})
