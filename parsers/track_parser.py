from parsers.parser import Parser
from music.track import Track

class TrackParser(Parser):
    def parse(self, tracks):
        parsed_tracks = []
        for track in tracks:
            album = track['track']['album']
            artists = track['track']['artists']
            track_id = track['track']['id']
            name = track['track']['name']
            popularity = track['track']['popularity']
            parsed_tracks.append(Track(album, artists, track_id, name, popularity))
        return parsed_tracks