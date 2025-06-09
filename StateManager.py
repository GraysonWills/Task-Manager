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
        return task_id in self.tasks

    def add_task_to_dict(self, task):
        self.tasks[task.id] = task

    def delete_task_from_dict(self, task_id):
        if self.check_for_task(task_id):
            del self.tasks[task_id]
    
    @property
    def shelfInformation(self):
        return self._shelfInformation
    
    @shelfInformation.setter
    def shelfInformation(self, shelfInformation):
        self._shelfInformation = shelfInformation

    def construct_shelf(self, password=None):
        if password:
            return {'password': password, 'tasks': self.tasks}
        else:
            return {'password': self.currentUser.password, 'tasks': self.tasks}
    
    