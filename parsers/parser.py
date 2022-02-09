from abc import abstractmethod


class Parser:

    @abstractmethod
    def parse(self, to_parse):
        pass