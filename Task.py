import random

class Task():

    def __init__(self, description):
        self._description = description
        self._completed = False
        self._id = round(random.random() * 1000)

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, new_description):
        self._description = new_description
    
    @property
    def completed(self):
        return self._completed
    
    @completed.setter
    def completed(self, new_completed):
        self._completed = new_completed

    @property
    def id(self):
        return self._id
                        
