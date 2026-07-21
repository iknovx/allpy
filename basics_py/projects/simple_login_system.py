import json

with open('basic/projects/jsons/login.json', 'r') as f:
    login_data = json.load(f)

def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        email = input("Enter your email: ")

        if (
            username == login_data['name'] or username == login_data['name1']
            and password == login_data['password'] or password == login_data['password1']
            and email == login_data['email'] or email == login_data['email1']
        ):
            print("Login successful!")

            with open('basic/projects/logs/log.txt', 'a') as f:
                f.write(f"User {username} logged in successfully.\n")

            return True

        print("Invalid username, password or email. Please try again.")

if __name__ == "__main__":
    login()