from music.exceptions.music_exceptions import AlbumAlreadyExistsException


class Artist:
    def __init__(self, artist_id, name, albums):
        self.artist_id = artist_id
        self.name = name
        self.albums = {}

    def add_album_to_artist(self, album):
        if album.album_id in self.albums:
            raise AlbumAlreadyExistsException
        else:
            self.albums[album.album_id] = album
