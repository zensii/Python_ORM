import os
from datetime import timedelta, date
import django
from django.utils.timezone import now

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Book, Author, Artist, Song, Product, Review, Driver, DrivingLicense, Owner, Registration, \
    Car


# Create queries within functions

def show_all_authors_with_their_books():
    result = []
    authors = Author.objects.all().order_by('id')
    for author in authors:
        author_books = author.books.all()
        if author_books:
            result.append(f"{author.name} has written - {', '.join([b.title for b in author_books])}!")
    return '\n'.join(result)

def delete_all_authors_without_books():

    all_authors = Author.objects.all()
    for author in all_authors:
        if not author.books.all():
            author.delete()

def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)

def get_songs_by_artist(artist_name: str):
    return Artist.objects.get(name=artist_name).songs.all().order_by('-id')

def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.remove(song)

def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    average_rating = sum(r.rating for r in product.reviews.all())/(product.reviews.count())
    return average_rating

def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)

def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')

def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()

def calculate_licenses_expiration_dates():
    result = []
    licenses = DrivingLicense.objects.all().order_by('-license_number')
    for l in licenses:
        expiration_date = l.issue_date + timedelta(days=365)
        result.append(f"License with number: {l.license_number} expires on {expiration_date}!")
    return '\n'.join(result)

def get_drivers_with_expired_licenses(due_date: date):
    expired = []
    licenses = DrivingLicense.objects.all()
    for l in licenses:
        expiration = l.issue_date + timedelta(days=365)
        if expiration > due_date:
            expired.append(l)
    return Driver.objects.filter(license__in=expired)

def register_car_by_owner(owner: Owner):
    first_free_registration = Registration.objects.filter(car__isnull=True).first()
    first_car_to_register = Car.objects.filter(registration__isnull=True).first()
    first_car_to_register.registration = first_free_registration
    first_car_to_register.owner = owner
    first_car_to_register.save()
    first_free_registration.registration_date = now()
    first_free_registration.save()

    return (f"Successfully registered {first_car_to_register.model} "
            f"to {first_car_to_register.owner.name} with"
            f" registration number {first_free_registration.registration_number}.")
