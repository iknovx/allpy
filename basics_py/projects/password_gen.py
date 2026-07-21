import json
from pathlib import Path
from random import randint, shuffle

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

PASSWORDS_PATH = Path(__file__).parent / "jsons" / "passwords.json"


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_password(nr_letters, nr_symbols, nr_numbers):
    password_list = []

    for _ in range(nr_letters):
        password_list.append(LETTERS[randint(0, len(LETTERS) - 1)])

    for _ in range(nr_symbols):
        password_list.append(SYMBOLS[randint(0, len(SYMBOLS) - 1)])

    for _ in range(nr_numbers):
        password_list.append(NUMBERS[randint(0, len(NUMBERS) - 1)])

    shuffle(password_list)
    return ''.join(password_list)


def save_password(password, path):
    if path.exists():
        with open(path) as f:
            try:
                saved = json.load(f)
            except json.JSONDecodeError:
                saved = []
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        saved = []

    saved.append({
    "password": password,
    "length": len(password),
    })

    with open(path, "w") as f:
        json.dump(saved, f, indent=2)


def main():
    user_choice = input("Do you want to generate a password? (yes/no): ").strip().lower()

    if user_choice not in ("yes", "y"):
        print("Password generation cancelled.")
        return

    nr_letters = get_positive_int("How many letters would you like in your password? ")
    nr_symbols = get_positive_int("How many symbols would you like? ")
    nr_numbers = get_positive_int("How many numbers would you like? ")

    if nr_letters + nr_symbols + nr_numbers == 0:
        print("Password would be empty — nothing to generate.")
        return

    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    print(f"Your generated password is: {password}")

    save_password(password, PASSWORDS_PATH)


if __name__ == "__main__":
    main()