import logging
from user.user import User
from music.playlist import Playlist


class PremiumUser(User):
    def __init__(self, username):
        super().__init__(username)

    def add_new_playlist(self, playlist_name):
        if playlist_name not in self.playlists:
            self.playlists[playlist_name] = Playlist(playlist_name)
        else:
            logging.warning("A playlist with this name already exists")

    def add_track_to_playlist(self, playlist_name, track_id, track_index):
        try:
            self.playlists[playlist_name].add_track(track_index.tracks[track_id])
        except KeyError:
            if playlist_name not in self.playlists:
                logging.error("Playlist does not exist")
            else:
                logging.error("Track ID does not exist")
