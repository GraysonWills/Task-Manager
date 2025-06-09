from ShelfService import ShelfService
from Task import Task
from StateManager import StateManager
from ThreadService import ThreadFactory
from User import User
from CryptographyService import CryptographyService
import UIPrompts as messages

class UIManager(CryptographyService, ThreadFactory, ShelfService, StateManager):

    def __init__(self):
        CryptographyService.__init__(self)
        ThreadFactory.__init__(self)
        ShelfService.__init__(self)
        StateManager.__init__(self)

    def register(self):
        while(True):
            username = self.encode_base64(input(messages.ENTER_USERNAME_REGISTER))
            if(self.checkForKey(username)):
                print(messages.USERNAME_EXISTS)
            else:
                break
        
        password = self.encode_base64(input(messages.ENTER_PASSWORD))
        self.currentUser = User(username, password)
        self.write(username, self.construct_shelf(password=password))
        print(messages.REGISTRATION_COMPLETE)

    def login(self):
        while(True):
            username = self.encode_base64(input(messages.ENTER_USERNAME_LOGIN))
            if(self.checkForKey(username)):
                information = self.read(username)
                self.tasks = information['tasks']
                break
            else:
                print(messages.USERNAME_NOT_EXIST)

        while(True):
            password = self.encode_base64(input(messages.ENTER_PASSWORD_LOGIN))
            if(password == information['password']):
                print(messages.LOGIN_SUCCESSFUL)
                self.currentUser = User(username, password)
                break
            else:
                print(messages.INCORRECT_PASSWORD)
            

    def add_task(self):
        taskDescription = input(messages.ENTER_TASK_DESCRIPTION)
        newTask = Task(taskDescription)
        self.add_task_to_dict(newTask)
        self.write(self.currentUser.username, self.construct_shelf())
        
    def display_table(self):
        print(messages.TASK_TABLE_HEADER)
        print(messages.TASK_TABLE_SEPARATOR)
        [print(f"{task.id}\t\t{task.description}\t\t{task.completed}") for task in self.tasks.values()]
        print(messages.TASK_TABLE_SEPARATOR + "\n")

    def view_tasks(self):
        self.display_table()

    def mark_as_complete(self):
        if not self.tasks:
            print(messages.NO_TASKS_FOUND)
            return
        
        self.display_table()
        id = self.take_id_input()
        self.tasks[id].completed = True
        self.write(self.currentUser.username, self.construct_shelf())

    def delete_task(self):
        if not self.tasks:
            print(messages.NO_TASKS_FOUND)
            return
        
        self.display_table()
        id = self.take_id_input()
        self.delete_task_from_dict(id)
        self.write(self.currentUser.username, self.construct_shelf())

    def take_id_input(self) -> int:
        while(True):
            try:
                task_id = int(input(messages.SELECT_TASK_ID))
                if(self.check_for_task(task_id)):
                    return task_id
                else:
                    print(messages.INVALID_TASK_ID)
            except ValueError:
                print(messages.INVALID_NUMBER_INPUT)
        

    def logout(self):
        self.write(self.currentUser.username, self.construct_shelf())
        print(messages.LOGOUT_MESSAGE)
        self.tasks = {}
        self.shelfInformation = {}
