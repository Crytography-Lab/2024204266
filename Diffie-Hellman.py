

p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

# Private keys
a = int(input("Enter Alice private key: "))
b = int(input("Enter Bob private key: "))

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("Alice public key:", A)
print("Bob public key:", B)

# Shared secret keys
key_A = pow(B, a, p)
key_B = pow(A, b, p)

print("Alice shared secret:", key_A)
print("Bob shared secret:", key_B)

if key_A == key_B:
    print("Key Exchange Successful!")
else:
    print("Key Exchange Failed!")
