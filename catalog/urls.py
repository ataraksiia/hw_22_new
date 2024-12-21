from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ProductInfoView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [path("", HomeView.as_view(), name="home"),
               path("product/<int:pk>/", ProductInfoView.as_view(), name="product_info"),
               path("contacts/", ContactsView.as_view(), name="contacts"),]

