from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.db import models

from main_app.managers import PublisherManager


class Publisher(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
    )
    established_date = models.DateField(
        default='1800-01-01',
    )
    country = models.CharField(
        max_length=40,
        default='TBC',
    )
    rating = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
    )
    objects = PublisherManager()

class Author(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=40,
        default='TBC',
    )
    is_active = models.BooleanField(
        default=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )



class Book(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Other', 'Other'),
    ]

    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2)],
    )
    publication_date = models.DateField()
    summary = models.TextField(
        blank=True,
        null=True,
    )
    genre = models.CharField(
        max_length=11,
        choices=GENRE_CHOICES,
        default='Other',
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01),
            MaxValueValidator(9999.99)
        ],
        default=0.01,
    )
    rating = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
    )
    is_bestseller = models.BooleanField(
        default=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='books',
    )
    main_author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='authored_books',

    )
    co_authors = models.ManyToManyField(
        Author,
        related_name='co_authored_books',
        blank=True,
    )


    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        if self.main_author in self.co_authors.all():
            self.co_authors.remove(self.main_author)
