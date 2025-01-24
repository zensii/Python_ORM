from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator
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