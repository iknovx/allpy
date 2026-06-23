from basics_py.projects.calculator import calculator
from basics_py.projects.simple_timer import timer


if __name__ == "__main__":
    print("Hello and welcome to menu")
    while True:
        print("Press 1 if you want to calculate something and 2 if you need timer: ")
        user_choice = int(input("Choose one of them: "))

        match user_choice:
            case 1:
                calculator()
            case 2:
                timer()
            case 3:
                print("The end")
                break
            case _:
                print("Invalid choice")
            