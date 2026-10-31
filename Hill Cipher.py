

import numpy as np

key = np.array([[3, 3], [2, 5]])

def encrypt(text):
    text = text.upper().replace(" ", "")

    if len(text) % 2 != 0:
        text += 'X'

    result = ""

    for i in range(0, len(text), 2):
        a = ord(text[i]) - 65
        b = ord(text[i+1]) - 65

        c1 = (key[0][0]*a + key[0][1]*b) % 26
        c2 = (key[1][0]*a + key[1][1]*b) % 26

        result += chr(c1 + 65) + chr(c2 + 65)

    return result

def decrypt(cipher):
    det = int(round(np.linalg.det(key)))
    det_inv = pow(det % 26, -1, 26)

    adj = np.array([[key[1][1], -key[0][1]],
                    [-key[1][0], key[0][0]]])

    inverse = (det_inv * adj) % 26

    result = ""

    for i in range(0, len(cipher), 2):
        a = ord(cipher[i]) - 65
        b = ord(cipher[i+1]) - 65

        p1 = (inverse[0][0]*a + inverse[0][1]*b) % 26
        p2 = (inverse[1][0]*a + inverse[1][1]*b) % 26

        result += chr(int(p1) + 65) + chr(int(p2) + 65)

    return result

message = input("Enter message: ")

cipher = encrypt(message)
print("Encrypted message:", cipher)
print("Decrypted message:", decrypt(cipher))
