# Simple Hospital Login System Prototype
# Academic illustration only

users = {
    "doctor1": "Password@123",
    "nurse1": "Nurse#456",
    "admin1": "Admin!789"
}

def authenticate(username, password):
    if username in users and users[username] == password:
        return True
    return False

def main():
    print("Hospital Login System")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if authenticate(username, password):
        print("Access granted.")
    else:
        print("Access denied.")

if __name__ == "__main__":
    main()
