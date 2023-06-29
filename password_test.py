#!/usr/bin/python3
import models
from models import storage
from models.farmer import Farmer
from models.base_model import BaseModel
from flask_bcrypt import generate_password_hash, check_password_hash


def test_password_hashing():
    # Get the password from the user during registration
    # user = storage.get(Farmer, 'a44daf8c-8a55-4b14-b356-90cc0dee7f27')
    user = storage.all(Farmer)
    print(user)

    # Hash the password
    hashed_password = user.hashed_password

    print("Hashed Password:", hashed_password)

    # Get the password from the user during authentication
    login_password = input("Enter login password: ")

    # Verify the password
    if user.email or check_password_hash(hashed_password.strip(), login_password.strip()):
        print("Authentication successful")
    else:
        print("Authentication failed")

if __name__ == '__main__':
    test_password_hashing()
