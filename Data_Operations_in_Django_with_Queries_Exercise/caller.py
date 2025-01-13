import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


def create_pet(name: str, species: str):
    Pet.objects.create(name=name, species=species)

    return f"{name} is a very cute {species}!"
# Create queries within functions

def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):

    new_artifact = Artifact(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    new_artifact.save()

    return f"The artifact {name} is {age} years old!"

def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()

def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    all_locations = Location.objects.all().order_by('-id')
    result = []
    for location in all_locations:
        result.append(f"{location.name} has a population of {location.population}!")
    return '\n'.join(result)

def new_capital():
    city_to_promote = Location.objects.first()
    city_to_promote.is_capital = True
    city_to_promote.save()

def get_capitals():
    capitals = Location.objects.filter(is_capital=True,)
    return capitals.values('name')

def delete_first_location():
    Location.objects.first().delete()

def apply_discount():
    cars = Car.objects.all()
    for car in cars:
        year = car.year
        discount = sum([int(digit) for digit in str(year)])
        car.price_with_discount = car.price - (car.price * discount / 100)
        car.save()

def get_recent_cars():
    return Car.objects.filter(year__gt='2020').values('model','price_with_discount')

def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    unfinished = Task.objects.filter(is_finished=False)
    return '\n'.join(str(task) for task in unfinished)


def complete_odd_tasks():

    tasks = Task.objects.all()
    odd_tasks = [task for task in tasks if task.id % 2 == 1]
    for task in odd_tasks:
        task.is_finished = True
    Task.objects.bulk_update(odd_tasks, ['is_finished'])

def encode_and_replace(text: str, task_title: str):
    tasks = Task.objects.filter(title=task_title)
    for task in tasks:
        task.description = ''.join(chr(ord(char)-3) for char in text)
        task.save()


def get_deluxe_rooms():
    result = []
    all_deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    for room in all_deluxe_rooms:
        if room.id % 2 == 0:
            result.append(str(room))
    return '\n'.join(result)

def increase_room_capacity():
    rooms = HotelRoom.objects.order_by('id')

    for number, room in enumerate(rooms):
        if room.is_reserved:
            if room.id == rooms[0].id:
                room.capacity += int(room.id)
            else:
                room.capacity += rooms[number-1].capacity
    HotelRoom.objects.bulk_update(rooms, ['capacity'])

def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()

def delete_last_room():
    last_room = HotelRoom.objects.last()
    if not last_room.is_reserved:
        last_room.delete()

def update_characters():
    all_chars = Character.objects.all()
    for char in all_chars:
        if char.class_name == 'Mage':
            char.level += 3
            char.intelligence -= 7
        elif char.class_name == 'Warrior':
            char.hit_points /= 2
            char.dexterity -= 4
        elif char.class_name in ['Assassin', 'Scout']:
            char.inventory = ' The inventory is empty'

    Character.objects.bulk_update(all_chars, ['level', 'intelligence', 'hit_points', 'dexterity', 'inventory'])


def fuse_characters(first_character: Character, second_character: Character):

    new_name = f"{first_character.name} {second_character.name}"
    new_class_name = 'Fusion'
    new_level = (first_character.level + second_character.level) // 2
    new_strength = (first_character.strength + second_character.strength) * 1.2
    new_dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    new_intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    new_hit_points = first_character.hit_points + second_character.hit_points
    new_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom" if\
        first_character.class_name in ['Mage', 'Scout'] else\
        "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=new_name,
        class_name=new_class_name,
        level=new_level,
        strength=new_strength,
        dexterity=new_dexterity,
        intelligence=new_intelligence,
        hit_points=new_hit_points,
        inventory=new_inventory
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)

def grand_strength():
    Character.objects.update(strength=50)

def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()
