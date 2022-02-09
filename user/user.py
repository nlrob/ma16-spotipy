from abc import abstractmethod


class User:
    def __init__(self, username, premium_status):
        self.username = username
        self.premium = premium_status
        self.playlists = {}

    @abstractmethod
    def add_new_playlist(self, playlist_name):
        pass

    @abstractmethod
    def add_track_to_playlist(self, playlist_name, track_id, track_index):
        pass