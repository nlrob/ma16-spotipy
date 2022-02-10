from extractors import *
from indexer import *
from parsers import *
from search import *
from user import *

src_dir = 'C:\\Test\\songs'
extractor = JsonTrackExtractor(src_dir)
track_index = TrackIndexer().index_tracks(TrackParser().parse(extractor.extract()))
album_index = AlbumIndexer().index_albums(track_index)
artist_index = ArtistIndexer().index_artists(album_index)

premium_user = UserFile('C:\\Test\\users.txt').get_user_object('premium_user')
free_user = UserFile('C:\\Test\\users.txt').get_user_object('free_user')

premium_search = Search(track_index, album_index, artist_index, premium_user)
free_search = Search(track_index, album_index, artist_index, free_user)

print(premium_search.get_artists())
print(free_search.get_artists())