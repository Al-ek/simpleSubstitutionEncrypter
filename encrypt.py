from pathlib import Path
from datetime import datetime
from substitutionEncryption import *
import os

waiting = True

while waiting:
    print("encrypt (e), decrypt (d), or keygen (k)?")
    choice = input()
    choice = choice[0]
    if choice != "e" and choice != "d" and choice != "k":
        print("Invalid choice")
    else:
        waiting = False

if choice == "k":
    keyname = input("Enter a name for your key: ")

    if Path("keys").exists():
        with open("keys/" + keyname, 'w') as f:
            print(keygen(), file=f, end="")
    else:
        os.mkdir("keys")
        with open("keys/" + keyname, 'w') as f:
            print(keygen(), file=f, end="")

elif choice == "e":
    keyFileName = input("Select key from the 'keys' dir: ")
    inputFileName = input("Select a file to encrypt: ")
    
    with open("keys/" + keyFileName, "r") as f:
        key = f.read()
    
    with open(inputFileName, "r") as f:
        contents = f.read()
        encryptedContents = encrypt(contents, key)

    if Path("outputs").exists():
        with open("outputs/" + str(datetime.now()), "w") as f:
            print(encryptedContents, file=f, end="")
    else:
        os.mkdir("outputs") 
        with open("outputs/" + inputFileName, "w") as f:
            print(encryptedContents, file=f, end="")

elif choice == "d": 
    keyFileName = input("Select key from the 'keys' dir: ")
    inputFileName = input("Select a file to decrypt: ")

    with open("keys/" + keyFileName, "r") as f:
        key = f.read()

    with open(inputFileName, "r") as f:
        contents = f.read()
        decryptedContents = decrypt(contents, key)
        print(decryptedContents)


