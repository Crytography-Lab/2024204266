

a = int(input("Enter a number: "))
b = int(input("Enter modulus: "))

if b <= 0:
    print("Modulus must be positive")
else:
    result = a % b
    print("Modular result is:", result)
