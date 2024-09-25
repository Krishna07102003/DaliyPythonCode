users = {
    "admin": "password",
    "user": "password"
}

def login():
    print("Login Page")
    print("-----------")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Logged in successfully")
    else:
        print("Invalid username or password")

def home():
    print("Home Page")
    print("---------")
    print("1. Login")
    choice = input("Enter your choice: ")
    if choice == "1":
        login()
    else:
        print("Invalid choice")

def main():
    while True:
        home()

if __name__ == "__main__":
    main()