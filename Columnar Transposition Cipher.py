

def encrypt(text, key):
    cols = len(key)
    rows = (len(text) + cols - 1) // cols

    text = text.ljust(rows * cols, 'X')

    matrix = [text[i:i+cols] for i in range(0, len(text), cols)]

    order = sorted(range(cols), key=lambda i: (key[i], i))

    cipher = ''

    for col in order:
        for row in matrix:
            cipher += row[col]

    return cipher


def decrypt(cipher, key):
    cols = len(key)
    rows = len(cipher) // cols

    order = sorted(range(cols), key=lambda i: (key[i], i))

    matrix = [[''] * cols for i in range(rows)]

    pos = 0

    for col in order:
        for row in range(rows):
            matrix[row][col] = cipher[pos]
            pos += 1

    return ''.join(''.join(row) for row in matrix).rstrip('X')


message = input("Enter message: ").replace(" ", "")
key = input("Enter keyword: ").upper()

if not key.isalpha():
    print("Keyword must contain only letters.")
else:
    cipher = encrypt(message, key)
    print("Encrypted message:", cipher)
    print("Decrypted message:", decrypt(cipher, key))
