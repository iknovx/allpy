import json

with open('basic/projects/login.json', 'r') as f:
    login_data = json.load(f)

def login(username:str , password:str) -> bool:
   username = input("Enter your username: ")
   password = input("Enter your password: ")
   
   while username != login_data['name'] or password != login_data['password']:
       print("Invalid username or password. Please try again.")
       username = input("Enter your username: ")
       password = input("Enter your password: ")
       if username == login_data['name'] and password == login_data['password']:
           print("Login successful!")
           return True
       elif username != login_data['name'] or password != login_data['password']:
            print("Invalid username or password. Please try again.")
       else:
            print("Login successful!")
            return True
    
    
    
    
if __name__ == "__main__":
    login("admin", "admin")