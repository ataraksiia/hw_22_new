from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(
            name="Xiaomi",
            description="Компания Xiaomi регулярно презентует гаджеты, "
            "стараясь угодить наибольшему количеству "
            "потенциальных клиентов.",
        )

        products = [
            {
                "name": "Xiaomi 14T Pro ",
                "description": "12/512GB титановый",
                "price": 79990,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added product: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product already exists: {product.name}")
                )
