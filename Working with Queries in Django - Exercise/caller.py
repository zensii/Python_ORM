import os
from typing import List

import django
from django.db.models import Case, When, Value

from main_app.choices import OperationSystemChoice

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal


# Create and check models
# Run and print your queries


def show_highest_rated_art() -> str:
    best_artwork = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return f"{best_artwork.art_name} is the highest-rated art with a {best_artwork.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    ArtworkGallery.objects.bulk_create([
        first_art,
        second_art,
    ])


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()
    # DELETE FROM artwork WHERE rating < 0


def show_the_most_expensive_laptop() -> str:
    most_expensive_laptop = Laptop.objects.order_by('-price', '-id').first()

    return f"{most_expensive_laptop.brand} is the most expensive laptop available for {most_expensive_laptop.price}$!"


def bulk_create_laptops(args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage() -> None:
    """
    UPDATE laptop
    SET storage = 512
    WHERE brand in (Asus, Lenovo)
    """

    Laptop.objects.filter(brand__in=("Asus", "Lenovo")).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=("Apple", "Dell", "Acer")).update(memory=16)


def update_operation_systems() -> None:
    # Solution 1
    Laptop.objects.update(
        operation_system=Case(
            When(brand="Asus", then=Value(OperationSystemChoice.WINDOWS)),
            When(brand="Apple", then=Value(OperationSystemChoice.MACOS)),
            When(brand__in=("Dell", "Acer"), then=Value(OperationSystemChoice.LINUX)),
            When(brand="Lenovo", then=Value(OperationSystemChoice.CHROME_OS))
        )
    )

    # Solution 2
    # Laptop.objects.filter(brand="Asus").update(operation_system=OperationSystemChoice.WINDOWS)
    # Laptop.objects.filter(brand="Apple").update(operation_system=OperationSystemChoice.MACOS)
    # Laptop.objects.filter(brand__in=("Dell", "Acer")).update(operation_system=OperationSystemChoice.LINUX)
    # Laptop.objects.filter(brand="Lenovo").update(operation_system=OperationSystemChoice.CHROME_OS)


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(args)

def delete_chess_players():
    ChessPlayer.objects.filter(title='no title').delete()

def change_chess_games_won():
    ChessPlayer.objects.filter(title='GM').update(games_won=30)

def change_chess_games_lost():
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)

def change_chess_games_drawn():
    ChessPlayer.objects.all().update(games_drawn=10)

def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')

def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title='IM')

def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title='FM')

def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__range=(0, 2199)).update(title='regular player')

def set_new_chefs():
    Meal.objects.update(
        chef=Case(
            When(meal_type='Breakfast', then=Value('Gordon Ramsay')),
            When(meal_type='Lunch', then=Value('Julia Child')),
            When(meal_type='Dinner', then=Value('Jamie Oliver')),
            When(meal_type='Snack', then=Value('Thomas Keller')),
        )
    )

def set_new_preparation_times():
    Meal.objects.update(
        preparation_time=Case(
            When(meal_type='Breakfast', then=Value('10 minutes')),
            When(meal_type='Lunch', then=Value('12 minutes')),
            When(meal_type='Dinner', then=Value('15 minutes')),
            When(meal_type='Snack', then=Value('5 minutes')),
        )
    )

def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=['Breakfast', 'Dinner']).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).delete()

