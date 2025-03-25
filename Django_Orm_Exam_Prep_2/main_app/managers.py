from django.db import models
from django.db.models import Count


class GetRegularsManager(models.Manager):
    def get_regular_customers(self):

        return (self.get_queryset()
        .annotate(orders_made=Count('profile_orders'))
        .filter(orders_made__gt=2)
        .order_by('-orders_made')
        )