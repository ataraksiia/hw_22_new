from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductCreateView, ProductDetailView, ContactTemplateView, HomeTemplateView,\
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

# urlpatterns = [path("", ProductListView.as_view(), name="home"),
#                path("product/<int:pk>/", ProductDetailView.as_view(), name="product_info"),
#                path("contacts/", ContactTemplateView.as_view(), name="contacts"),]

urlpatterns = [path("", ProductListView.as_view(), name="home"),
               path('contacts/', ContactTemplateView.as_view(), name='contacts'),
               path('product/<int:pk>/', ProductDetailView.as_view(), name="product_info"),
               path('product/create/', ProductCreateView.as_view(), name='product_create'),
               path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
               path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_confirm_delete'), ]
