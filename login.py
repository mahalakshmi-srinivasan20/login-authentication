users = {}

def register(username, password):
    if username in users:
        print("Username already exists. Please choose a different username.")
    else:
        users[username] = password
        print("Registration successful.")

def login(username, password):
    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Login failed. Please check your username and password.")
        return False

while True:
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = input("Select an option: ")

    if choice == '1':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        register(username, password)
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login(username, password):
            print("Access granted to secured page.")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please select again.")
