from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import DirectorManager
from main_app.mixins import AwardedMixin, UpdatedMixin


# Create your models here.

class BaseModel(models.Model):

    full_name = models.CharField(
        max_length=120,
        validators=(
            MinLengthValidator(limit_value=2),
        ),
    )

    birth_date = models.DateField(default='1900-01-01')

    nationality = models.CharField(
        max_length=50,
        default='Unknown',
    )

    class Meta:
        abstract = True


class Director(BaseModel):

    years_of_experience = models.SmallIntegerField(
        default=0,
        validators=(
            MinValueValidator(limit_value=0),
        )
    )

    objects = DirectorManager()

class Actor(BaseModel,AwardedMixin,UpdatedMixin):
    ...


class Movie(AwardedMixin, UpdatedMixin):

    class MovieGenres(models.TextChoices):

            ACTION = 'Action', 'Action'
            COMEDY = 'Comedy', 'Comedy'
            DRAMA = 'Drama', 'Drama'
            OTHER = 'Other', 'Other'


    title = models.CharField(
        max_length=150,
        validators=(
            MinLengthValidator(limit_value=5),
        ),
    )

    release_date = models.DateField()

    storyline = models.TextField(null=True, blank=True)

    genre = models.CharField(
        choices=MovieGenres.choices,
        max_length=6,
        default=MovieGenres.OTHER,
        )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=(
            MinValueValidator(limit_value=0.0),
            MaxValueValidator(limit_value=10.0),
        )
    )

    is_classic = models.BooleanField(default=False)

    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name='director_movies',
    )

    starring_actor = models.ForeignKey(
        Actor,
        on_delete=models.SET_NULL,
        null=True,
        related_name='starring_movies',
    )

    actors = models.ManyToManyField(
        Actor,
        related_name='actor_movies'
    )


