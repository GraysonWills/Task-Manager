class User:
    def __init__(self, username, password):
        self._username = username
        self.__password = password
    
    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self.__password
    
