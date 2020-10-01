class C(object):
    def __init__(self):
        self.dict = {"brand": "Ford","model": "Mustang","year": 1964}
    def execute(self):
        sorted = {"values": self.dict.sort()}
        return sorted
