import string, random

ALPHABET = string.ascii_letters + string.punctuation + string.digits + " "

def encrypt(text, key):
    encText = ""

    for ch in text:
        idx = ALPHABET.find(ch)
        if idx == -1:
            encText += ch  # leave unchanged
        else:
            encText += key[idx]

    return encText

def keygen():
    key = ""
    alphabet = ALPHABET

    for i in range(len(ALPHABET) - 1, -1, -1):
        
        idx = random.randint(0, i)
        key = key + alphabet[idx]
        alphabet = alphabet.replace(alphabet[idx], "")

    return key

def decrypt(text, key):
    decText = ""

    for ch in text:
        idx = key.find(ch)
        if idx == -1:
            decText += ch  # leave unchanged
        else:
            decText += ALPHABET[idx]

    return decText
