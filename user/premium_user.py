import logging
from user.user import User



class PremiumUser(User):
    def __init__(self, username):
        super().__init__(username)

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
