

def rc4(key, message):
    key = key.encode()
    message = message.encode()

    S = list(range(256))
    j = 0

    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    result = []

    for byte in message:
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        k = S[(S[i] + S[j]) % 256]

        result.append(byte ^ k)

    return bytes(result)


key = input("Enter secret key: ")
message = input("Enter message: ")

if not key:
    print("Key cannot be empty.")
else:
    encrypted = rc4(key, message)

    print("Encrypted message:", encrypted.hex())

    decrypted = rc4(key, encrypted.decode('latin-1'))

    print("Decrypted message:", decrypted.hex())
