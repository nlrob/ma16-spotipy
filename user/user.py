from abc import abstractmethod


class User:
    def __init__(self, username):
        self.username = username
        self.playlists = {}

    @abstractmethod
    def add_new_playlist(self, playlist_name):
        pass

    @abstractmethod
    def add_track_to_playlist(self, playlist_name, track_id, track_index):
        pass