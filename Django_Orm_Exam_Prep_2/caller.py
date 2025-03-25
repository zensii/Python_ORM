import os
import django
from django.db.models import Q, Count, F

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

def get_profiles(search_string=None):
    if search_string is not None:
        search_results = Profile.objects.filter(
            Q(full_name__icontains=search_string) |
            Q(email__icontains=search_string) |
            Q(phone_number__icontains=search_string)
        ).order_by("full_name")

        return '\n'.join([
                f"Profile: {result.full_name}, "
                f"email: {result.email}, "
                f"phone number: {result.phone_number}, "
                f"orders: {result.profile_orders.count()}"
                for result in search_results
        ])

    return ''


def get_loyal_profiles():
    results = Profile.objects.get_regular_customers()

    if results:
        return '\n'.join([
            f"Profile: {customer.full_name}, "
            f"orders: {customer.orders_made}"
            for customer in results
        ])
    return ''


def get_last_sold_products():
    last_order = Order.objects.all().order_by('-creation_date').first()

    if last_order:
        return f"Last sold products: {', '.join([product.name for product in last_order.products.all()])}"
    return ''


def get_top_products():
    # Get products that appear in ANY order (completed or not)
    top_products = (
        Product.objects
        .annotate(
            times_sold=Count('product_orders')  # Count orders containing the product
        )
        .filter(times_sold__gt=0)  # Exclude never-ordered products
        .order_by('-times_sold', 'name')[:5]  # Get top 5 after ordering
    )

    if not top_products:
        return ""

    result = ["Top products:"]
    for product in top_products:
        result.append(f"{product.name}, sold {product.times_sold} times")


    return '\n'.join(result)


def apply_discounts():

    orders_to_discount = (
        Order.objects
        .filter(is_completed=False)
        .annotate(num_products=Count('products'))
        .filter(num_products__gt=2)
    )

    update_count = orders_to_discount.update(
        total_price=F('total_price') * 0.9
    )

    return f"Discount applied to {update_count} orders."


def complete_order():
    to_complete = Order.objects.filter(is_completed=False).order_by('creation_date').first()
    if to_complete:

        for product in to_complete.products.all():
            product.in_stock -= 1
            product.save()

        to_complete.products.filter(in_stock=0).update(is_available=False)
        to_complete.is_completed = True
        to_complete.save()

        return f"Order has been completed!"
    return ''

