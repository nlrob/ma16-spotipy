import json
import os
import logging
from extractors.file_extractor import FileExtractor


class JsonTrackExtractor(FileExtractor):
    def __init__(self, src_directory):
        self.src_directory = src_directory


    def extract(self):
        extracted_jsons = []
        try:
            for file in os.listdir(self.src_directory):
                with open(f'{self.src_directory}\\{file}') as json_track:
                    extracted_jsons.append(json.load(json_track))
            return extracted_jsons
        except FileNotFoundError:
            logging.error("Directory doesn't exist")