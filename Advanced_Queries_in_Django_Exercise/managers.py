from decimal import Decimal

from django.db import models
from django.db.models import Count, Avg



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

# class VideoGameManager(models.Manager):
#
#     def games_by_genre(self, genre: str):
#
#         return self.filter(genre=genre)
#
#     def recently_released_games(self, year: int):
#
#         return self.filter(release_year__gte=year)
#
#
#     def highest_rated_game(self):
#
#         return self.order_by('-rating').first()
#
#
#     def lowest_rated_game(self):
#
#         return self.order_by('rating').first()
#
#
#     def average_rating(self):
#
#         avg_rating = self.aggregate(average_rating=Avg('rating'))
#         return f"{avg_rating['average_rating']:.1f}"

class VideoGameManager(models.Manager):
    def games_by_genre(self, genre: str):
        return self.filter(genre=genre)

    def recently_released_games(self, year: int):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):

        return self.order_by('-rating').first()

    def lowest_rated_game(self):
        return self.order_by('rating').first()

    def average_rating(self) -> str:

        average_rating = self.aggregate(average_rating=Avg('rating'))['average_rating']
        return f"{average_rating:.1f}"










































