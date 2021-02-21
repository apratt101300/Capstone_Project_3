import artworkDB
from menu import Menu
import view


def main():
    setup()
    menu = make_menu()
    while True:
        choice = view.show_menu_get_choice(menu)
        function = menu.get_function(choice)
        function()
        if choice == 'Q':
            break


        
def setup():
    artworkDB.create_database()


def make_menu():
    menu = Menu()
    menu.add_menu_option('1', 'Add new artist.', add_artist)
    menu.add_menu_option('2', 'Search by artist.', search_by_artist)
    menu.add_menu_option('3', 'Search available art by artist.', search_available_by_artist)
    menu.add_menu_option('4', 'Add artwork.', add_artwork)
    menu.add_menu_option('5', 'Delete artwork.', delete_artwork)
    menu.add_menu_option('6', 'Change artwork availability.', change_availability)
    menu.add_menu_option('Q', 'Quit program.', quite_program)
    return menu


def add_artist():
    artist_name = view.get_user_input('What\'s the name of the new artist?')
    artist_email = view.get_user_input('What\'s the artist\'s email address?')
    artworkDB.add_artist(artist_name, artist_email)


def search_by_artist():
    artist_name = view.get_user_input('What\'s the name of the artist you want to search for?')
    artworks = artworkDB.search_artwork_by_artist(artist_name)
    for art in artworks:
        print(f'Artist: {art.artist} Name: {art.name} Price: {art.price}')


def search_available_by_artist():
    pass


def add_artwork():
    pass


def delete_artwork():
    pass


def change_availability():
    pass


def quite_program():
    print('GOODBYE.')

if __name__ == "__main__":
    main()
