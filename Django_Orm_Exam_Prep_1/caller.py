import os
from decimal import Decimal

import django
from django.db import models
from django.db.models import Q, F
from django.db.models.aggregates import Avg
from django.db.models.functions import Least

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Actor, Director, Movie
# Create queries within functions

def populate_db():
    director_1 = Director.objects.create(
        full_name='Ivan Ivanov',
        birth_date='1987-05-08',
        nationality='Bulgaria',
        years_of_experience=10,
    )
    director_2 = Director.objects.create(
        full_name='Ivan Petrov',
        birth_date='1983-05-08',
        nationality='Serbia',
        years_of_experience=15,
    )
    director_3 = Director.objects.create(
        full_name='John Smith',
        birth_date='1969-01-24',
        nationality='USA',
        years_of_experience=20,
    )

    actor_1 = Actor.objects.create(
        full_name='Gosho Goshev',
        birth_date='2001-01-11',
        nationality='Bulgaria',
        is_awarded=True,
    )

    actor_2 = Actor.objects.create(
        full_name='Petya Milanova',
        birth_date='1999-02-12',
        nationality='Bulgaria',
        is_awarded=False,
    )

    actor_3 = Actor.objects.create(
        full_name='Jhonny Bravo',
        birth_date='1977-04-25',
        nationality='USA',
        is_awarded=True,
    )

    movie_1 = Movie.objects.create(
        title='The Dumb Movie',
        release_date = '2024-01-01',
        storyline='A dumb action movie about nothing',
        genre='Action',
        rating='0.1',
        is_classic=False,
        is_awarded=False,
        director=director_1,
        starring_actor=actor_1,
        # actors = (actor_1, actor_2,)
    )
    movie_1.actors.add(actor_1, actor_2)

    movie_2 = Movie.objects.create(
        title='Rush Hour',
        release_date = '2024-09-11',
        storyline='An action packed movie about cars',
        genre='Action',
        rating='5.7',
        is_classic=True,
        is_awarded=False,
        director=director_3,
        starring_actor=actor_2,
        # actors = (actor_2, actor_3,)
    )
    movie_2.actors.add(actor_2, actor_3)

    movie_3 = Movie.objects.create(
        title='The Matrix',
        release_date = '1999-03-31',
        storyline='A science fiction movie about machines',
        genre='Action',
        rating='9.8',
        is_classic=True,
        is_awarded=True,
        director=director_2,
        starring_actor=actor_1,
        # actors = (actor_1, actor_2,  actor_3,)
    )
    movie_3.actors.add(actor_1, actor_2, actor_3)

def get_directors(search_name=None, search_nationality=None):
    director_obj = Director.objects.all()
    filters = Q()
    if not search_name and not search_nationality:
        return ''
    if search_name:
        filters &= Q(full_name__icontains=search_name)
    if search_nationality:
        filters &= Q(nationality__icontains=search_nationality)

    results = [
        (f"Director: {director.full_name}, "
         f"nationality: { director.nationality}, "
         f"experience: {director.years_of_experience}"
         ) for director in director_obj.filter(filters).order_by('full_name')
    ]

    return '\n'.join(results)


def get_top_director():

    best = Director.objects.get_directors_by_movies_count().first()
    if best:
        return f"Top Director: {best.full_name}, movies: {best.movies_count}."
    return ''


def get_top_actor():

    best = Actor.objects.all()
    top_actor = (best.annotate(
        starred_movies_count=models.Count('starring_movies'))
                 .order_by('-starred_movies_count', 'full_name')
                 .first()
                 )
    if not top_actor:
        return ''

    starred_in = top_actor.starring_movies.all()
    if not starred_in:
        return ''

    return (f"Top Actor: {top_actor.full_name}, "
            f"starring in movies: {', '.join(movie.title for movie in starred_in)}, "
            f"movies average rating: {top_actor.starring_movies.aggregate(Avg('rating'))['rating__avg']:.1f}"
            )


def get_actors_by_movies_count():
    actors = Actor.objects.all().filter(actor_movies__isnull=False)

    if not actors:
        return ''

    top_3 = (actors.annotate(
        starred_movies_count=models.Count('actor_movies'))
                 .order_by('-starred_movies_count', 'full_name')[:3]
                 )
    result = [f"{actor.full_name}, participated in {actor.starred_movies_count} movies" for actor in top_3]
    return '\n'.join(result)


def get_top_rated_awarded_movie():

    top = Movie.objects.filter(is_awarded=True).order_by('-rating', 'title').first()

    if not top:
        return ''

    return (f"Top rated awarded movie: {top.title}, "
            f"rating: {top.rating:.1f}. "
            f"Starring actor: {top.starring_actor.full_name if top.starring_actor else 'N/A'}. "
            f"Cast: {', '.join(actor.full_name for actor in top.actors.all().order_by('full_name'))}.")
print(get_top_rated_awarded_movie())

# def increase_rating():
#
#     classics = Movie.objects.filter(is_classic=True, rating__lt=10.0)
#
#     if not classics:
#         return "No ratings increased."
#
#     for classic in classics:
#         classic.rating = min(10.0, classic.rating + Decimal(0.1))
#         classic.save()
#
#     return f"Rating increased for {len(classics)} movies."


def increase_rating():
    # Get classics and update in one query
    updated = Movie.objects.filter(
        is_classic=True,
        rating__lt=10.0
    ).update(
        rating=Least(10.0, F('rating') + Decimal('0.1'))
    )

    return f"Rating increased for {updated} movies." if updated else "No ratings increased."