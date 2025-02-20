from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductCreateView, ProductDetailView, ContactTemplateView, HomeTemplateView, \
    ProductUpdateView, ProductDeleteView, ProductListByCategoryView

app_name = CatalogConfig.name

urlpatterns = [path("", ProductListView.as_view(), name="home"),
               path('contacts/', ContactTemplateView.as_view(), name='contacts'),
               path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name="product_info"),
               path('product/create/', ProductCreateView.as_view(), name='product_create'),
               path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
               path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_confirm_delete'),
               path('category/<int:category_id>/', ProductListByCategoryView.as_view(), name='product_list_by_category'),
               ]
