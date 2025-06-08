class StateManager:
    def __init__(self):
        self._currentUser = None
        self._tasks = None

        @property
        def currentUser(self):
            return self._currentUser
        
        @currentUser.setter
        def currentUser(self, currentUser):
            self._currentUser = currentUser
        
        @property
        def tasks(self):
            return self._tasks
        
        @tasks.setter
        def tasks(self, tasks):
            self._tasks = tasks
