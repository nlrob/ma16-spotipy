from music.exceptions.music_exceptions import ArtistAlreadyExistsException


class ArtistIndex:
    def __init__(self):
        self.artists = {}

    def add_artist(self, artist):
        if artist.artist_id in self.artists:
            raise ArtistAlreadyExistsException
        else:
            self.artists[artist.artist_id] = artist
