def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input())

num2 = int(input())
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")

