from music.indexes.album_index import AlbumIndex
from music.album import Album
from music.exceptions.music_exceptions import AlbumAlreadyExistsException


class AlbumIndexer:
    def index_albums(self, track_index):
        album_index = AlbumIndex()
        for track in track_index.tracks.keys():
            new_album = Album(track_index.tracks[track].album['id'],track_index.tracks[track].album['name'],
                              track_index.tracks[track].artists[0]['id'])
            try:
                album_index.add_album(new_album)
            except AlbumAlreadyExistsException:
                pass
            finally:
                album_index.albums[track_index.tracks[track].album['id']].add_track_to_album(track_index.tracks[track])
        return album_index
