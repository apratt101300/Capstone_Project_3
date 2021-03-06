from models import Artist, Artwork, db
from peewee import IntegrityError


"""Functions in this module interact with the database"""

def create_database():
    db.connect()
    db.create_tables([Artist, Artwork])


def add_artist(name, email):
    new_artist = Artist(name=name, email=email)
    new_artist.save()


def add_artwork(artist, name, price, availability):
    try:
        artist_id = _get_artist_id(artist)
        new_artwork = Artwork(artist=artist_id, name=name, price=price, available=availability)
        new_artwork.save()
        return f'The artwork \'{name}\' by {artist} was added successfully.'
    except IntegrityError:
        return 'I\'m sorry. There was an issue adding this art.'


def delete_artwork(artwork_name):
    Artwork.delete().where(Artwork.name == artwork_name).execute()


def change_availability(artwork_name, availability):
    Artwork.update(available=availability).where(Artwork.name == artwork_name).execute()


def search_artwork_by_artist(name):
    artworks = Artwork.select().join(Artist).where(Artist.name == name)
    return artworks


def search_available_by_artist(name):
    artworks = Artwork.select().join(Artist).where((Artist.name == name) & (Artwork.available == True))
    return artworks


def get_all_artwork():
    artwork = Artwork.select()
    return artwork


def _get_artist_id(name):
   artist = Artist.get_or_none(Artist.name == name) 
   artist_id = artist.id
   return artist_id


















