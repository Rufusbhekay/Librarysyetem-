from cryptography.fernet import Fernet 

master_pwd = input("what is the master password? ")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines(): 
            data = line.rstrip()   
            user, passw = data.split("|")
            print("User:", user, " | password:", passw)
    

def add():
    name = input("Account Name: ")
    pwd = input("password: ")
    print("Account added succesfully")
    
    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd )


while True: 
    mode = input("Would you like to add a new password/view your password/press q to quit: ")
    if mode == "q": 
        break 

    elif mode == "view": 
        view()
    elif mode == "add": 
        add()
    else: 
        print("invalid mode")
        continue 



