


def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch
    return result

def decrypt(text, key):
    return encrypt(text, -key)

message = input("Enter message: ")
key = int(input("Enter key: "))

cipher = encrypt(message, key)
print("Encrypted message:", cipher)
print("Decrypted message:", decrypt(cipher, key))
