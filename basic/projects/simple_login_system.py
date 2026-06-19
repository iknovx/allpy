import json

with open('basic/projects/jsons/login.json', 'r') as f:
    login_data = json.load(f)

def login(username:str , password:str, email:str) -> bool:
   username = input("Enter your username: ")
   password = input("Enter your password: ")
   email = input("Enter your email: ")
   
   while username != login_data['name'] or password != login_data['password'] or email != login_data['email']:
       print("Invalid username or password. Please try again.")
       username = input("Enter your username: ")
       password = input("Enter your password: ")
       email = input("Enter your email: ")
       if username == login_data['name'] and password == login_data['password'] and email == login_data['email']:
           print("Login successful!")
           return True
       elif username != login_data['name'] or password != login_data['password'] or email != login_data['email']:
            print("Invalid username or password or email. Please try again.")
       else:
            print("Login successful!")
            return True
    
    
    
    
if __name__ == "__main__":
    login("admin", "admin", "admin")