from music.exceptions.music_exceptions import AlbumAlreadyExistsException


class AlbumIndex:
    def __init__(self):
        self.albums = {}

    def add_album(self, album):
        if album.album_id in self.albums:
            raise AlbumAlreadyExistsException
        else:
            self.albums[album.album_id] = album
