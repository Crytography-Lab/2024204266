

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Generate 8-byte DES key
key = get_random_bytes(8)

def encrypt(message):
    cipher = DES.new(key, DES.MODE_CBC)
    ciphertext = cipher.encrypt(
        pad(message.encode(), DES.block_size)
    )
    return cipher.iv, ciphertext

def decrypt(iv, ciphertext):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = unpad(
        cipher.decrypt(ciphertext),
        DES.block_size
    )
    return plaintext.decode()

message = input("Enter message: ")

iv, encrypted = encrypt(message)

print("Secret Key:", key.hex())
print("Encrypted Message:", encrypted.hex())
print("Decrypted Message:", decrypt(iv, encrypted))
