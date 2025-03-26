from decimal import Decimal

from django.db import models
from django.db.models import Sum, Count


class RealEstateListingManager(models.Manager):

    def by_property_type(self,property_type: str):

        return self.get_queryset().filter(property_type=property_type)

    def in_price_range(self, min_price: Decimal, max_price: Decimal):

        return self.get_queryset().filter(price__gte=min_price, price__lte=max_price)

    def with_bedrooms(self, bedrooms_count: int):

        return self.get_queryset().filter(bedrooms=bedrooms_count)

    def popular_locations(self):

        return self.get_queryset().values(
            'location'
        ).annotate(
            location_count=Count('id')
        ).order_by(
            '-location_count','location'

        )[:2]




