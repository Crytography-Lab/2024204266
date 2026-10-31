

a = int(input("Enter a number: "))
m = int(input("Enter modulus: "))

if m > 1 and __import__('math').gcd(a, m) == 1:
    inverse = pow(a, -1, m)
    print("Multiplicative Inverse:", inverse)
else:
    print("Inverse does not exist")
