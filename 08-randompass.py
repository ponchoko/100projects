import random
import string

def main():
    length = int(input("Enter password length: "))
    ok = string.ascii_letters + string.digits + string.punctuation
    passw = ''.join(random.choice(ok) for i in range(length))
    print("passowrd is ", passw)

main()