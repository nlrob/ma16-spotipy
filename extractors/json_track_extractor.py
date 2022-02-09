import json
import os
from extractors.file_extractor import FileExtractor


class JsonTrackExtractor(FileExtractor):
    def __init__(self, src_directory):
        self.src_directory = src_directory

    def extract(self):
        extracted_jsons = []
        for file in os.listdir(self.src_directory):
            with open(file) as json_track:
                extracted_jsons.append(json.load(json_track))
        return extracted_jsons