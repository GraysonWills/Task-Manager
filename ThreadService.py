from threading import Thread
from queue import Queue

class ThreadFactory:
    def __init__(self):
        self._asyncQueue = Queue()
    
    def createThread(self, target, args):
        return Thread(target=target, args=args)
    