

a = int(input("Enter a number: "))
p = int(input("Enter a prime number: "))

if p > 1 and all(p % i != 0 for i in range(2, int(p**0.5) + 1)) and a % p != 0:
    result = pow(a, p - 1, p)
    print("Result:", result)
    print("Fermat's Little Theorem verified")
else:
    print("Invalid input")
