

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate 16-byte AES key
key = get_random_bytes(16)

def encrypt(message):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(
        message.encode()
    )
    return cipher.nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode()

message = input("Enter message: ")

nonce, encrypted, tag = encrypt(message)

print("Secret Key:", key.hex())
print("Encrypted Message:", encrypted.hex())
print("Decrypted Message:", decrypt(nonce, encrypted, tag))
