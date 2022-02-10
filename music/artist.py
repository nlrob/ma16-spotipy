import logging
from music.exceptions.music_exceptions import AlbumAlreadyExistsException
from user.user import User


class Artist (User):
    def __init__(self, artist_id, name, albums):
        super().__init__(name)
        self.artist_id = artist_id
        self.name = name
        self.albums = {}

    def add_album_to_artist(self, album):
        if album.album_id in self.albums:
            raise AlbumAlreadyExistsException
        else:
            self.albums[album.album_id] = album

        def add_new_playlist(self, playlist_name):
            super().add_new_playlist(playlist_name)

    def add_track_to_playlist(self, playlist_name, track_id, track_index):
        try:
            self.playlists[playlist_name].add_track(track_index.tracks[track_id])
        except KeyError:
            if playlist_name not in self.playlists:
                logging.error("Playlist does not exist")
            else:
                logging.error("Track ID does not exist")
