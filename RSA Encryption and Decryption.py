

p = 3
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 3
d = pow(e, -1, phi)

message = int(input("Enter message number (0 to 32): "))

if 0 <= message < n:
    # Encryption
    cipher = pow(message, e, n)
    print("Encrypted message:", cipher)

    # Decryption
    decrypted = pow(cipher, d, n)
    print("Decrypted message:", decrypted)
else:
    print("Message must be between 0 and 32.")
