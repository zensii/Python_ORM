import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here


from main_app.models import Animal, Mammal, Bird, Reptile

# Animal.objects.create(name="Nemo", species="Clownfish", birth_date="2019-04-10", sound="Bubbles")
# Mammal.objects.create(name="Fluffy", species="Orangutan", birth_date="2018-02-10", sound="Chomps", fur_color="Reddish-brown")
# Bird.objects.create(name="Robby", species="American Robin", birth_date="2021-03-20", sound="Chirp", wing_span=28.50)
# Reptile.objects.create(name="Python", species="Ball Python", birth_date="2019-07-01", sound="Hiss", scale_type="Smooth")
#
# animals = Animal.objects.all()
# for a in animals:
#     print(f"{a.name}: {a.species}.")


from main_app.models import ZooKeeper, Veterinarian

# Keep the data from the previous exercise, so you can reuse it
#
# zookeeper = ZooKeeper.objects.create(first_name="Peter", last_name="Johnson", phone_number="0899524265", specialty="Mammals")
# mammal = Mammal.objects.get(name="Fluffy")
# zookeeper.managed_animals.add(mammal)
# veterinarian = Veterinarian.objects.create(first_name="Dr. Michael", last_name="Smith", phone_number="9876543210", license_number="VET12345")
#
# zookeeper_from_db = ZooKeeper.objects.first()
# print(f"{zookeeper_from_db.first_name} {zookeeper_from_db.last_name} is a ZooKeeper.")
#
# veterinarian_from_db = Veterinarian.objects.first()
# print(f"{veterinarian_from_db.first_name} {veterinarian_from_db.last_name} is a Veterinarian.")

from main_app.models import ZooKeeper
#
# zookeeper = ZooKeeper(first_name="John", last_name="Doe", phone_number="0123456789", specialty="Fishes")
# zookeeper.full_clean()
# zookeeper.save()


from main_app.models import ZooDisplayAnimal
#
# # Keep the data from the previous exercises, so you can reuse it
#
# all_animals_info = ZooDisplayAnimal.objects.all()
# for a in all_animals_info:
#     print(a.display_info())
#     print(a.is_endangered())


# from main_app.models import Veterinarian
#
# v1 = Veterinarian.objects.create(first_name="John", last_name="Doe", phone_number="0896625120", license_number="VET123", availability=False)
# print(v1.availability)
# v2 = Veterinarian.objects.create(first_name="Alice", last_name="Johnson", phone_number="0896529728", license_number="VET789")
# print(v2.availability)
