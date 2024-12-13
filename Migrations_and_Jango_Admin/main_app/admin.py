from django.contrib import admin
from main_app.models import Product

# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass