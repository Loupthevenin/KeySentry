import json
import os
from cryptography.fernet import Fernet


class KeySentry:
    def __init__(self):
        self.files = []

    def open_data(self):
        for file in os.listdir():
            if ".json" in file:
                file_data = file
        with open(file_data, "r") as file_json:
            data = json.load(file_json)
        return data

    def save_data(self, data):
        with open("data.json", "w") as file_json:
            json.dump(data, file_json, indent=4)

    def files(self):
        for file in os.listdir():
            if file == "api.py" or file == "main.py" or file == "key.key":
                continue
            if os.path.isfile(file):
                self.files.append(file)

    def crypt(self):
        key = Fernet.generate_key()
        with open("key.key", "wb") as thekey:
            thekey.write(key)

        with open("data.json", "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open("data.json", "wb") as thefile:
            thefile.write(contents_encrypted)

    def decrypt(self):
        with open("key.key", "rb") as key:
            secretkey = key.read()

        with open("data.json", "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open("data.json", "wb") as thefile:
            thefile.write(contents_decrypted)

    def show_key(self):
        with open("key.key", "rb") as key:
            secretkey = key.read()
        return print(secretkey)
