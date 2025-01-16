import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Book, Author
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

# Create authors
author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George Orwell")
author3 = Author.objects.create(name="Harper Lee")
author4 = Author.objects.create(name="Mark Twain")

# Create books associated with the authors
book1 = Book.objects.create(
    title="Harry Potter and the Philosopher's Stone",
    price=19.99,
    author=author1
)
book2 = Book.objects.create(
    title="1984",
    price=14.99,
    author=author2
)

book3 = Book.objects.create(
    title="To Kill a Mockingbird",
    price=12.99,
    author=author3
)

# Display authors and their books
authors_with_books = show_all_authors_with_their_books()
print(authors_with_books)

# Delete authors without books


delete_all_authors_without_books()
print(Author.objects.count())
