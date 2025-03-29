import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Publisher,Book,Author

def populate_db():

    publisher1 = Publisher.objects.create(
        name="Penguin Books",
        established_date="1935-07-30",
        country="United Kingdom",
        rating=4.5
    )

    publisher2 = Publisher.objects.create(
        name="HarperCollins",
        established_date="1989-03-10",
        country="United States",
        rating=4.2
    )

    author1 = Author.objects.create(
        name="J.K. Rowling",
        birth_date="1965-07-31",
        country="United Kingdom",
        is_active=True
    )

    author2 = Author.objects.create(
        name="George R.R. Martin",
        birth_date="1948-09-20",
        country="United States",
        is_active=True
    )

    author3 = Author.objects.create(
        name="Agatha Christie",
        birth_date="1890-09-15",
        country="United Kingdom",
        is_active=False
    )

    author4 = Author.objects.create(
        name="Stephen King",
        birth_date="1947-09-21",
        country="United States",
        is_active=True
    )

    book1 = Book.objects.create(
        title="Harry Potter and the Philosopher's Stone",
        publication_date="1997-06-26",
        summary="A young boy discovers he's a wizard and attends Hogwarts School of Witchcraft and Wizardry.",
        genre="Fiction",
        price=12.99,
        rating=4.8,
        is_bestseller=True,
        publisher=publisher1,
        main_author=author1
    )
    book1.co_authors.add(author3)

    book2 = Book.objects.create(
        title="A Game of Thrones",
        publication_date="1996-08-01",
        summary="Noble families fight for control of the mythical land of Westeros.",
        genre="Fiction",
        price=15.50,
        rating=4.7,
        is_bestseller=True,
        publisher=publisher2,
        main_author=author2
    )
    book2.co_authors.add(author4)

    book3 = Book.objects.create(
        title="The Shining",
        publication_date="1977-01-28",
        summary="A family heads to an isolated hotel for the winter where a sinister presence influences the father.",
        genre="Fiction",
        price=10.99,
        rating=4.6,
        is_bestseller=True,
        publisher=publisher1,
        main_author=author4
    )

    book4 = Book.objects.create(
        title="Murder on the Orient Express",
        publication_date="1934-01-01",
        summary="Detective Hercule Poirot investigates a murder on a luxury train.",
        genre="Fiction",
        price=9.99,
        rating=4.4,
        is_bestseller=False,
        publisher=publisher2,
        main_author=author3
    )
