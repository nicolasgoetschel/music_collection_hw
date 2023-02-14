from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

def select_all():
    albums = []
    sql = "SELECT * FROM album"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = album(row['title'], artist, row['genre'], row['id'] )
        album.append(album)
    return album


    