from save_data_sql import Users
import os
import hashlib

users = Users()

# SignUP
def signup():
    while True:
        name = input("-Name: ")
        name_upper = name.upper()

        names = users.names()
        ls_names = [x[0] for x in names]
        if name_upper in ls_names:
            print("-This name used (Please enter another name)")
            continue
        else:
            break 

    surname = input("-Surname: ")
    while True:
        email = input("-E-mail: ")
        emails = users.emails()
        ls_emails = [x[0] for x in emails]
        if email in ls_emails:
            print("-This E-mail used (Please enter another E-mail)")
            continue
        else:
            break 

    while True:
        password = input("-Password: ")
    
        if len(password) < 8:
            print("-Password length lower than 8")
            continue
        else:
            break
    

    salt = os.urandom(16).hex()       

    while True:
        password_again = input("-Password again: ")

        if password == password_again:
            print("-Successful signup")
            break
        else:
            print("-Please input password again correctly")
            continue
    
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    users.add_user(name_upper, surname, email, hashed_password, salt)

# Login
def login():
    while True:
        name = input("-Name: ")
        name_upper = name.upper()
        password = input("-Password: ")

        names = users.names()
        ls_names = [x[0] for x in names]

        if name_upper not in ls_names:
            print("-User not found")
            continue

        info = users.users_info(name_upper)
        dtb_password = info[0]
        dtb_salt = info[1]   
        password_attempt = hashlib.sha256((password + dtb_salt).encode()).hexdigest()

        if password_attempt == dtb_password:
            print("-Successful login")
            break 
        if not name:
            print("-Please input name")
            continue
        if not password:
            print("-Please input password")
            continue
        else:
            print("-Name or password incorrect")
            continue


while True:
    print('''--------SignUp Login system--------
        Enter 0 for Sign up 
        Enter 1 for Login
        Enter x for close the program''')


    choice = input("-Enter: ")
    if choice not in ["0", "1", "x"]:
        print('-Please enter (0 ,1 or x)')
        continue
        
    if choice == "0":
        print("------SignUp------")
        signup()
        continue

    if choice == "1":
        print("------Login------")
        login()
        break    

    if choice == "x":
        print("-Program closed")
        break