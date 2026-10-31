

a1 = int(input("Enter first remainder: "))
m1 = int(input("Enter first modulus: "))

a2 = int(input("Enter second remainder: "))
m2 = int(input("Enter second modulus: "))

if m1 <= 0 or m2 <= 0:
    print("Moduli must be positive")
elif __import__('math').gcd(m1, m2) != 1:
    print("Moduli must be coprime")
else:
    M = m1 * m2
    M1 = M // m1
    M2 = M // m2

    x = (a1 * M1 * pow(M1, -1, m1) +
         a2 * M2 * pow(M2, -1, m2)) % M

    print("CRT Result:", x)
