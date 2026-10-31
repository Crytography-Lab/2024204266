

n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if __import__('math').gcd(i, n) == 1:
        count += 1

print("Euler's Totient:", count)
