import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Book, Author, Artist, Song


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
