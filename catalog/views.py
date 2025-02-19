from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_info.html'

    def get_object(self):
        post = super().get_object()
        post.view_counter += 1
        post.save()
        return post


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:product_info', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm("catalog.can_delete_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user

        if product.owner != user and not user.has_perm('catalog.can_delete_product'):
            raise PermissionDenied("Вы не можете удалять этот продукт.")

        return product
