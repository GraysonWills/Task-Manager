class StateManager:
    def __init__(self):
        self._currentUser = None
        self._tasksDictionary = {}
        self._shelfInformation = {}

        @property
        def currentUser(self):
            return self._currentUser
        
        @currentUser.setter
        def currentUser(self, currentUser):
            self._currentUser = currentUser
        
        @property
        def tasks(self):
            return self._tasksDictionary
        
        @tasks.setter
        def tasks(self, tasks):
            self._tasksDictionary = tasks

        def check_for_task(self, task_id):
            return task_id in tasks

        def add_task_to_dict(self, task):
            self._tasksDictionary[task.id] = task

        def delete_task(self, task):
            if task.id in self._tasksDictionary:
                del self._tasksDictionary[task.id]
        
        @property
        def shelfInformation(self):
            return self._shelfInformation
        
        @shelfInformation.setter
        def shelfInformation(self, shelfInformation):
            self._shelfInformation = shelfInformation

        def construct_shelf(self, password): 
            return {'password': password, 'tasks': tasks}