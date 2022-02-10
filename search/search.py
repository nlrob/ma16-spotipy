import logging
from user.free_user import FreeUser


class Search:
    def __init__(self, song_index, album_index, artist_index, user):
        self.song_index = song_index
        self.album_index = album_index
        self.artist_index = artist_index
        self.user = user

    def limit_results(self, search_results):
        if isinstance(self.user, FreeUser):
            return search_results[:5]
        else:
            return search_results

    def get_artists(self):
        search_result = []
        for artist in self.artist_index.artists.keys():
            search_result.append(self.artist_index.artists[artist].name)
        return self.limit_results(search_result)

    def get_albums_from_artist(self, artist_id):
        search_result = []
        try:
            artist = self.artist_index.artists[artist_id]
        except KeyError:
            logging.error("Artist does not exist in index")
        else:
            for album  in artist.albums.keys():
                search_result.append(artist.albums[album].name)
        return self.limit_results(search_result)

    def get_tracks_from_album(self, album_id):
        search_result = []
        try:
            album = self.album_index.albums[album_id]
        except KeyError:
            logging.error("Album does not exist in index")
        else:
            for track in album.tracks.keys():
                search_result.append(album.tracks[track].name)
        return self.limit_results(search_result)

