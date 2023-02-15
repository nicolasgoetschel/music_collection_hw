import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Bruce Springsteen")
artist_repository.save(artist1)

artist2 = Artist("Coldplay")
artist_repository.save(artist2)

album1 = Album("Born to Run", "Rock")
album_repository.save(album1)

album2 = Album("Parachutes", "Pop")
album_repository.save(album2)

album3 = Album("Mylo Xyloto", "Pop")
album_repository.save(album3)


# artist_repository.select_all()
pdb.set_trace()