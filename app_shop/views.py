from django.shortcuts import render
from django.views.generic import ListView, DetailView

from app_shop.models import Product
# Create your views here.


class Home(ListView):
    model = Product
    template_name = 'App_Shop/product_list.html'
