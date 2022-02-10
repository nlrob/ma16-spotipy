import logging
from music.playlist import Playlist


class User:
    def __init__(self, username):
        self.username = username
        self.playlists = {}

    def add_new_playlist(self, playlist_name):
        if playlist_name not in self.playlists:
            self.playlists[playlist_name] = Playlist(playlist_name)
        else:
            logging.warning("A playlist with this name already exists")

    def add_track_to_playlist(self, playlist_name, track_id, track_index):
        pass