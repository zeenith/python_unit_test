from test import MotDePasseValide

if __name__ == '__main__':
    pwd = input("Enter your password : ")
    valid_pwd = MotDePasseValide(pwd)
    if valid_pwd.isValid():
        print("Good Password")
    else:
        print("Bad Password")