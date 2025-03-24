import os
import django

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

