from django.db import models
from django.db.models import TextField, CASCADE


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40)

class Book(models.Model):
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')


class Song(models.Model):
    title = models.CharField(max_length=100, unique=True)

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    songs = models.ManyToManyField(Song, related_name='artists')


class Product(models.Model):
    name = models.CharField(max_length=100)

class Review(models.Model):
    description = TextField(max_length=200)
    rating = models.PositiveIntegerField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='reviews')

