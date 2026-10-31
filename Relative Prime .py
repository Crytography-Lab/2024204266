

import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if math.gcd(a, b) == 1:
    print("Numbers are Relatively Prime")
else:
    print("Numbers are Not Relatively Prime")
