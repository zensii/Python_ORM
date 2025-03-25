import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Order, Product, Profile


# Create queries within functions

def populate_db():

    profile_1 = Profile.objects.create(
        full_name="John Doe",
        email="jd@gmail.com",
        phone_number="1234567890",
        address = "123 Main St",
    )

    profile_2 = Profile.objects.create(
        full_name="John Doe",
        email="jd@gmail.com",
        phone_number="1234567890",
        address = "123 Main St",
    )

    product_1 = Product.objects.create(
        name="some product",
        description="some description",
        price=10.00,
        in_stock=10,
    )

    product_2 = Product.objects.create(
        name="some other product",
        description="some other description",
        price=20.00,
        in_stock=20,
    )

    order_1 = Order.objects.create(
        profile=profile_1,
        total_price=100.00,
        is_completed=True,
    )

    order_1.products.add(product_1)
    order_1.products.add(product_2)

    order_2 = Order.objects.create(
        profile=profile_2,
        total_price=200.00,
    )
    order_2.products.add(product_1)
    order_2.products.add(product_1)

populate_db()