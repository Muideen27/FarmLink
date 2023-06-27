#!/usr/bin/python3
from models import storage
from models.farmer import Farmer
from werkzeug.security import check_password_hash

user_id = 'a44daf8c-8a55-4b14-b356-90cc0dee7f27'
user = storage.get(Farmer, user_id)

print(user)

login_password = input("Enter login password: ")
hashed_password = user.hashed_password

if check_password_hash(hashed_password, login_password):
    print("Authentication successful")
else:
    print("Authentication failed")
