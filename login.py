from class_definitions import User

def create_user():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    password_candidate = input("Enter password: ")
    password_candidate2 = input("Re-enter password: ")
    if password_candidate == password_candidate2:
        password = password_candidate
    return User(name, phone, email, password)

def authenticate_user(user):
    password_candidate = input("Enter password: ")
    if password_candidate == user.password:
        return True
    else:
        return False

