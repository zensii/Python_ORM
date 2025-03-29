from django.db import models
from django.db.models.aggregates import Count


class PublisherManager(models.Manager):
    def get_publishers_by_books_count(self):

        return (self.get_queryset()
        .annotate(
            num_books=Count('books')
        )
        .order_by('-num_books', 'name'))



