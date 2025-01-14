import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery
# Create and check models
# Run and print your queries

def show_highest_rated_art() -> str:
    highest_rated = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f"{highest_rated.art_name} is the highest-rated art with a {highest_rated.rating} rating!"

def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    to_create = [first_art, second_art]
    ArtworkGallery.objects.bulk_create(to_create)

def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()


# artwork1 = ArtworkGallery(artist_name='Vincent van Gogh', art_name='Starry Night', rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name='Leonardo da Vinci', art_name='Mona Lisa', rating=5, price=1500000.0)
#
# # Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)
# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())
