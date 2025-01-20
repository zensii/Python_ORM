from datetime import datetime, date, timedelta
from django.core.exceptions import ValidationError
from django.db import models



# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

    @property
    def age(self):
        today = date.today()
        delta = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            delta -= 1
        return delta

class Mammal(Animal):
    fur_color = models.CharField(max_length=50)

class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)

class Reptile(Animal):
    scale_type = models.CharField(max_length=50)

class  Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        abstract=True

class Specialities(models.TextChoices):
    MAMMALS = "Mammals", "Mammals"
    BIRDS = "Birds", "Birds"
    REPTILES = "Reptiles", "Reptiles"
    OTHERS = "Others", "Others"

class ZooKeeper(Employee):
    specialty = models.CharField(max_length=10, choices=Specialities.choices)
    managed_animals = models.ManyToManyField(to=Animal, related_name='animals')

    def clean(self):
        if self.specialty not in Specialities:
            raise ValidationError('Specialty must be a valid choice.')


class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)


class ZooDisplayAnimal(Animal):

    class Meta:
        proxy=True

    def display_info(self):
        return f"Meet {self.name}! Species: {self.species}, born {self.birth_date}. It makes a noise like '{self.sound}'."

    def is_endangered(self):
        endangered = ["Cross River Gorilla", "Orangutan", "Green Turtle"]

        if self.species in endangered:
            return f"{self.species} is at risk!"
        return f"{self.species} is not at risk."
