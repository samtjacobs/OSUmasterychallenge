import os, random, struct
from Crypto.Cipher import AES

INIT = 'This is an IV456'

def get_key():
    key = input("Enter Key\n")
    if len(key) > 32:
        key = key[0:32]
    while len(key) % 8 != 0 or len(key) < 16:
        key += ' '
    return key


def write():
    key = get_key()
    obj = AES.new(key, AES.MODE_CBC, INIT)
    message = input("Enter Message\n")
    while len(message) % 16 != 0:
        message += ' '
    global cipher
    cipher = obj.encrypt(message)
    print("Your encrypted message as byte literal:")
    print(cipher)

    pass


def read():
    key = get_key()
    obj = AES.new(key, AES.MODE_CBC, INIT)
    try:
        message = obj.decrypt(cipher)
    except NameError:
        print("No message found")
    else:
        print("Your message is:")
        try:
            print(message.decode("utf-8"))
        except UnicodeDecodeError:
            print("Can't decode to utf-8, printing byte literal")
            print(message)
    pass


def main():
    while(True):
        choice = input("r/w/q?\n")
        if(choice is 'r'):
            read()
        elif(choice is 'w'):
            write()
        elif(choice is 'q'):
            exit(0)

if __name__ == "__main__":
    main()