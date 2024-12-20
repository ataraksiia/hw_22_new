from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, product_info

app_name = CatalogConfig.name

urlpatterns = [path("", home, name="home"),
               path("product/<int:pk>/", product_info, name="product_info")]

