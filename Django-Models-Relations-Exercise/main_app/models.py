from django.db import models
from django.db.models import TextField, CASCADE, PositiveIntegerField


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

class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class DrivingLicense(models.Model):
    license_number = models.CharField(max_length=10, unique=True)
    issue_date = models.DateField()
    driver = models.OneToOneField(to=Driver, on_delete=CASCADE, related_name='license')

class Owner(models.Model):
    name = models.CharField(max_length=50)

class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    owner = models.OneToOneField(to=Owner, on_delete=models.CASCADE, related_name='cars', blank=True, null=True)


class Registration(models.Model):
    registration_number = models.CharField(max_length=10, unique=True)
    registration_date = models.DateField(blank=True, null=True)
    car = models.OneToOneField(to=Car, on_delete=models.CASCADE, related_name='registration', blank=True, null=True)