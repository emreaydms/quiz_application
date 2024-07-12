from pymongo import MongoClient
import bcrypt

connection_string = 
client = MongoClient(connection_string)

db = client.quiz_application
users = db.users

def username_checker(username):
    global users
    user = users.find_one({"username": username})
    return user

def hasher(password):
    password = password.encode("utf-8")
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed

def register():
    global users

    while True:
        f_name = input("First Name>")
        if not len(f_name) == 0:
            break
    while True:
        l_name = input("Last Name>")
        if not len(l_name) == 0:
            break
    while True:
        username = input("Choose a Username>")
        if username_checker(username) == None:
            break
        else:
            print("This Username is Taken.")
    while True:
        password = input("Enter Your Password. Must Contain at Least 4 Characters>")
        if len(password) >= 4:
            break
    while True:
        p_confirm = input("Confirm Your Password>")
        if p_confirm == password:
            break
        else:
            print("Passwords Do Not Match.")

    user = {
        "name": f"{f_name} {l_name}",
        "username": username,
        "password": hasher(password),
        "quizzes":[]
    }
    users.insert_one(user)
    print("Registration Completed Successfully.")

def log_in():
    global users
    while True:
        username = input("Username>")
        if username_checker(username) == None:
            print("User Could Not Found.")
        else:
            break
    user = username_checker(username)
    while True:
        password = input("Password>")
        if bcrypt.checkpw(password.encode("utf-8"), user["password"]):
            break
        else:
            print("Password is Wrong.")
    print("Logged in Succesfully")
    return user

def log_out():
    return None







