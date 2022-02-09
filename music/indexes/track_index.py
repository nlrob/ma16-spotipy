from music.exceptions.music_exceptions import TrackAlreadyExistsException


class TrackIndex:
    def __init__(self):
        self.tracks = {}

    def add_track(self, track):
        if track.track_id in self.tracks:
            raise TrackAlreadyExistsException
        else:
            self.tracks[track.track_id] = track