from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''
def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key



key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data =line.rstrip()
            user, passw = data.split("|")
            print("User : ",user,",Password: ",fer.encrypt(passw.encode()).decode())

def add():
    name = input("Account name : ")
    pwd = input("password : ")
    with open('password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() +"\n")
while True:
    mode = input("Do you want to add new password or view existing password or press q to quite?(view,add,q) ").lower()

    if mode =="q":
        break
    if mode == "add":
        add()

    elif mode == "view":
        view()
    else:
        print("Invalid mode")
        continue