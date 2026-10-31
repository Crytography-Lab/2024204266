

import math

p = int(input("Enter first prime number: "))
q = int(input("Enter second prime number: "))

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    e += 1

d = pow(e, -1, phi)

print("Public Key:", (e, n))
print("Private Key:", (d, n))
print("RSA Key Generation Successful")
