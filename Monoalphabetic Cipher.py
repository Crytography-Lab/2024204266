

import string

plain = string.ascii_uppercase
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

def encrypt(text):
    result = ""
    for ch in text.upper():
        if ch in plain:
            result += key[plain.index(ch)]
        else:
            result += ch
    return result

def decrypt(text):
    result = ""
    for ch in text.upper():
        if ch in key:
            result += plain[key.index(ch)]
        else:
            result += ch
    return result

message = input("Enter message: ")

cipher = encrypt(message)
print("Encrypted message:", cipher)
print("Decrypted message:", decrypt(cipher))
