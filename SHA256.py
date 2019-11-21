import hashlib

import bcrypt as bcrypt
bcrypt
password = input("Input the password to hash\n")

print("\nSHA256:\n")
for i in range (3):
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.sha256(setpass)
    guess_pw = hash_object.hexdigest()
    print(guess_pw)