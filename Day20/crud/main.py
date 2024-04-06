from create import create_students
from update import update_students
from delete import delete_students
from read import read_students


def main():
    
    
    def exit_message():
        print("Thanks you\n see you again")
    
    choice = input("enter your choice c/r/u/d/e")
    choice = choice.lower()
    
    if choice == "c":
        create_students()
        count = create_students()
        main() if count else exit_message()
    elif choice == "r":
        read_students()
        count = read_students()
        main() if count else exit_message()
    elif choice == "u":
        update_students()
    elif choice =="d":
        delete_students()
    else:
        exit_message()
        
if __name__ == "__main__":
    main()