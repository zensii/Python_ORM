import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet,Artifact,Location


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

