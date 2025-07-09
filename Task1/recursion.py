def factorial(n):
    if n == 0:
        return 1
    elif n != 0:
        return n * factorial(n-1)

x = int(input("Enter a number: "))
b = factorial(x)
print(b)
