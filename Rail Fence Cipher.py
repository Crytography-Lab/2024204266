

def encrypt(text, rails):
    fence = ['' for i in range(rails)]
    row = 0
    direction = 1

    for ch in text:
        fence[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(fence)


def decrypt(cipher, rails):
    pattern = []
    row = 0
    direction = 1

    for i in range(len(cipher)):
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    counts = [pattern.count(i) for i in range(rails)]
    fence = []
    pos = 0

    for count in counts:
        fence.append(list(cipher[pos:pos+count]))
        pos += count

    result = ''
    indexes = [0] * rails

    for r in pattern:
        result += fence[r][indexes[r]]
        indexes[r] += 1

    return result


message = input("Enter message: ")
rails = int(input("Enter number of rails: "))

if rails < 2:
    print("Number of rails must be at least 2")
else:
    cipher = encrypt(message, rails)
    print("Encrypted message:", cipher)
    print("Decrypted message:", decrypt(cipher, rails))
