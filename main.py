from UIManager import UIManager
import UIPrompts as messages

def main():
    uiManager = UIManager()
    
    while(True):
        
        print(messages.WELCOME_MAIN)
        
        while(True):
            
            print(messages.MAIN_MENU_OPTIONS)

            choice = input(messages.ENTER_CHOICE)
            if choice == "1":
                uiManager.login()
                break
            elif choice == "2":
                uiManager.register()
                break
            elif choice == "3":
                print(messages.FAREWELL)
                return
            else:
                print(messages.INVALID_CHOICE)

        print(messages.WELCOME_TASK_MANAGER)
        
        while(True):

            print(messages.TASK_MENU_OPTIONS)

            choice = input(messages.ENTER_CHOICE)
            if choice == "1":
                uiManager.add_task()
            elif choice == "2":
                uiManager.view_tasks()
            elif choice == "3":
                uiManager.mark_as_complete()
            elif choice == "4":
                uiManager.delete_task()
            elif choice == "5":
                uiManager.logout()
                break
            else:
                print(messages.INVALID_CHOICE)

if __name__ == "__main__":
    main()
