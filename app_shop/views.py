from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from app_shop.models import Product
# Create your views here.


class Home(ListView):
    model = Product
    template_name = 'app_shop/home.html'


class ProductDetails(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'app_shop/product_details.html'
