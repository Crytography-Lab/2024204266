

def encrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('A')
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
            j += 1
        else:
            result += ch

    return result

def decrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('A')
            result += chr((ord(ch) - 65 - shift) % 26 + 65)
            j += 1
        else:
            result += ch

    return result

message = input("Enter message: ")
key = input("Enter keyword: ")

if not key.isalpha():
    print("Keyword must contain only letters.")
else:
    cipher = encrypt(message, key)
    print("Encrypted message:", cipher)
    print("Decrypted message:", decrypt(cipher, key))
