from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ProductInfoView(DetailView):
    model = Product
    template_name = 'catalog/product_info.html'


class ContactsView(ListView):
    model = Product
    template_name = 'catalog/contacts.html'

