from django.urls import path
from . import views

urlpatterns = [
    path("products/table/", views.product_table, name="product_table"),
    path("products/grid/", views.product_grid, name="product_grid"),
]
