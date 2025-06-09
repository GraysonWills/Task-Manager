from UIManager import UIManager

def main():
    uiManager = UIManager()
    
    while(True):
        
        print("Welcome To Our Task Manager App\n")
        
        while(True):
            print("1. Login")
            print("2. Register")
            print("3. Exit\n")

            choice = input("Please Enter Your Choice: ")
            if choice == "1":
                uiManager.login()
                break
            elif choice == "2":
                uiManager.register()
                break
            elif choice == "3":
                print("Farewell!\n")
                return
            else:
                print("Invalid choice. Please try again.\n")

        print("Welcome To Your Task Manager App\n")
        
        while(True):

            print("1. Add a task")
            print("2. View Tasks")
            print("3. Mark Task As Complete")
            print("4. Delete Task")
            print("5. Logout\n")

            choice = input("Please Enter Your Choice: ")
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
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
