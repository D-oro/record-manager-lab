import pdb

from models.album import Album
import repositories.album_repository as album_repository

from models.artist import Artist
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Lopez")
artist_2 = Artist("J-lo")

artist_repository.save(artist_1)
artist_repository.save(artist_2)

result = artist_repository.select_all()

for artist in result:
    print(artist.__dict__)

found_artist = artist_repository.select(artist_1.id)
print(found_artist.__dict__)


# albums

album_1 =  Album("somealbumtitle", "rock", artist_1)
album_repository.save(album_1)

result = album_repository.select_all()

for album in result:
    print(album.__dict__)

found_album = album_repository.select(album_1.id)
print(found_album.__dict__)


