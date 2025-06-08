import shelve
import queue
class ShelfService:
    def __init__(self):
        self._fileName = "userInfo"

    def read(self, key):
        with shelve.open(self._fileName) as shelf:
            return shelf[key]
    
    def write(self, key, data):
        with shelve.open(self._fileName) as shelf:
            shelf[key] = data

    def checkForKey(self, key) -> bool:
        with shelve.open(self._fileName) as shelf:
            return key in shelf
            