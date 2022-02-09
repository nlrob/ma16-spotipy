import logging
from music.indexes.track_index import TrackIndex
from music.exceptions.music_exceptions import TrackAlreadyExistsException


class TrackIndexer:
    def index_tracks(self, tracks_to_index):
        track_index = TrackIndex()
        for track in tracks_to_index:
            try:
                track_index.add_track(track)
            except TrackAlreadyExistsException:
                logging.warning("Track already exists in index")
        return track_index
