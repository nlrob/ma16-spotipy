from music.exceptions.music_exceptions import TrackAlreadyExistsException


class Album:
    def __init__(self, album_id, name, artist_id):
        self.album_id = album_id
        self.name = name
        self.artist_id = artist_id
        self.tracks = {}

    def add_track_to_album(self, track):
        if track.track_id in self.tracks:
            raise TrackAlreadyExistsException
        else:
            self.tracks[track.track_id] = track
