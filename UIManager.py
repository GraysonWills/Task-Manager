from ShelfService import ShelfService
from Task import Task
from StateManager import StateManager
from ThreadService import ThreadFactory
from User import User
from CryptographyService import CryptographyService
class UIManager(CryptographyService, ThreadFactory, ShelfService, StateManager):

    def __init__(self):
        CryptographyService.__init__(self)
        ThreadFactory.__init__(self)
        ShelfService.__init__(self)
        StateManager.__init__(self)

    def register(self):
        while(True):
            username= self.encode_base64(input("Welcome! Please Register With A UNIQUE Username: "))
            if(self.checkForKey(username)):
                print("Username already exists. Please try again.\n")
            else:
                break
        
        password = self.encode_base64(input("Please Enter A Password: "))
        self.currentUser = User(username, password)
        self.write(username, self.construct_shelf(password=password))
        print("Registration Complete!\n")

    def login(self):
        while(True):
            username = self.encode_base64(input("Please Enter Your Username: "))
            if(self.checkForKey(username)):
                information = self.read(username)
                self.tasks = information['tasks']
                break
            else:
                print("Username does not exist. Please try again.\n")

        while(True):
            password = self.encode_base64(input("Please Enter Your Password: "))
            if(password == information['password']):
                print("Login Successful!\n")
                self.currentUser = User(username, password)
                break
            else:
                print("Incorrect password. Please try again.\n")
            

    def add_task(self):
        taskDescription = input("Please Enter A Description For Your Task: ")
        newTask = Task(taskDescription)
        self.add_task_to_dict(newTask)
        self.write(self.currentUser.username, self.construct_shelf())
        
    def display_table(self):
        print("Task ID\t\tTask Description\t\tCompleted")
        print("---------------------------------------------------")
        [print(f"{task.id}\t\t{task.description}\t\t{task.completed}") for task in self.tasks.values()]
        print("---------------------------------------------------\n")

    def view_tasks(self):
        self.display_table()

    def mark_as_complete(self):
        if not self.tasks:
            print("No tasks found. Please add a task first.\n")
            return
        self.display_table()
        id = self.take_id_input()
        self.tasks[id].completed = True
        self.write(self.currentUser.username, self.construct_shelf())

    def delete_task(self):
        if not self.tasks:
            print("No tasks found. Please add a task first.\n")
            return
        self.display_table()
        id = self.take_id_input()
        self.delete_task_from_dict(id)
        self.write(self.currentUser.username, self.construct_shelf())

    def take_id_input(self) -> int:
        while(True):
            try:
                task_id = int(input("Select any id from the list: "))
                if(self.check_for_task(task_id)):
                    return task_id
                else:
                    print("Invalid input. Please pick an id in the list.\n")
            except ValueError:
                print("Invalid input. Your input must be a number\n")
        

    def logout(self):
        self.write(self.currentUser.username, self.construct_shelf())
        print("Thank You For Using Our Service! Your Current State Has Been Saved!")
        self.tasks = {}
        self.shelfInformation = {}
