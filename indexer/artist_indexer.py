from music.indexes.artist_index import ArtistIndex
from music.artist import Artist
from music.exceptions.music_exceptions import ArtistAlreadyExistsException

class ArtistIndexer:
    def index_artists(self, album_index):
        artist_index = ArtistIndex()
        for album in album_index.albums.keys():
            new_artist = Artist(album_index.albums[album].artist_id, album_index.albums[album].artist_name, None)
            try:
                artist_index.add_artist(new_artist)
            except ArtistAlreadyExistsException:
                pass
            finally:
                artist_index.artists[album_index.albums[album].artist_id].add_album_to_artist(album_index.albums[album])
        return artist_index