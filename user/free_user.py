import logging
from user.user import User


class FreeUser(User):
    def __init__(self, username):
        super().__init__(username)
        self.playlist_limit = 5
        self.track_limit = 20

    def add_new_playlist(self, playlist_name):
        if len(self.playlists) >= self.playlist_limit:
            logging.warning(f"Non-premium artists cannot create more than {self.playlist_limit} playlists at a time")
        else:
            super().add_new_playlist(playlist_name)

    def add_track_to_playlist(self, playlist_name, track_id, track_index):
        if len(self.playlists) >= self.track_limit:
            logging.warning(f"Non-premium users cannot add more than {self.track_limit} tracks to a playlist")
        else:
            super().add_track_to_playlist(playlist_name, track_id, track_index)
