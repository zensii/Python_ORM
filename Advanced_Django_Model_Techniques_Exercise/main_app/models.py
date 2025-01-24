from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator
from django.db import models

# Create your models here.

def name_validator(value: str):
    """
    Validates that the name contains only letters and/or spaces
    """
    if not value.replace(' ', 'x').isalpha():
        raise ValidationError("Name can only contain letters and spaces")


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            name_validator,
        ]
    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(18, "Age must be greater than or equal to 18"),
        ]
    )
    email = models.EmailField(
        error_messages={'invalid': 'Enter a valid email address'}
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(r'^\+359\d{9}$', "Phone number must start with '+359' followed by 9 digits"),
        ]
    )
    website_url = models.URLField(
        error_messages={'invalid': 'Enter a valid URL'}
    )

class BaseMedia(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True
        ordering=['-created_at', 'title']  # here using () instead of [] caused one test in Judge to fail.

class Book(BaseMedia):
    author = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, "Author must be at least 5 characters long")
        ]
    )
    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            MinLengthValidator(6, "ISBN must be at least 6 characters long")
        ]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Book'
        verbose_name_plural = 'Models of type - Book'

class Movie(BaseMedia):
    director = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(8, "Director must be at least 8 characters long")
        ]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Movie'
        verbose_name_plural = 'Models of type - Movie'

class Music(BaseMedia):
    artist = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(9, "Artist must be at least 9 characters long"),
        ]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Music'
        verbose_name_plural = 'Models of type - Music'


