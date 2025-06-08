from threading import Thread

class ThreadFactory:
    def __init__(self):
        pass
    
    def createThread(self, target, args):
        return Thread(target=target, args=args)
    