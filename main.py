#Holds user interface, runs program
from creator import charCreator


def main():
    print("You can either: \n\t1. Create a character  \n\t2. Exit the program.")
    choice = input("What do you want to do?(1/2): ")
    if choice == "1":
        charCreator()
    elif choice == "2":
        pass

main()