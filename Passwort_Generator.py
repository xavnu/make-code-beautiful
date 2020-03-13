

import random

X = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890^?!?$%&/()=?`'+#*'~';:_,.-<>|"
pwd = ""

print("Use Char list = %s \n" % X)

length = int(input("\n [*] Input Password Length: "))
while len(pwd) != length:
    pwd = pwd + random.choice(X)
    if len(pwd) == length:
        print("Password: %s\n" % pwd)
