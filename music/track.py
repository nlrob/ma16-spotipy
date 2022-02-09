class Track:
    def __init__(self, track):
        self.album = track['album']
        self.artists = track['artists']
        self.id = track['id']
        self.name = track['name']
        self.popularity = track['popularity']
