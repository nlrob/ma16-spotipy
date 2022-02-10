class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)