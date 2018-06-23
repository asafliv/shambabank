from abc import abstractmethod


class DataSourceScraper:

    def __init__(self):
        pass

    @abstractmethod
    def login(self):
        raise NotImplementedError("Should have implemented this")

    @abstractmethod
    def pull(self):
        raise NotImplementedError("Should have implemented this")

    @abstractmethod
    def parse(self):
        raise NotImplementedError("Should have implemented this")

    @abstractmethod
    def combine(self):
        raise NotImplementedError("Should have implemented this")

    @abstractmethod
    def upload(self):
        raise NotImplementedError("Should have implemented this")
