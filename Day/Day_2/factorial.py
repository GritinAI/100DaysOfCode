num = int(input("Enter a Number to find the Factorial: "))

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return factorial(n-1) * n

fact = factorial(n = num)

print(f"The Factorial for {num} is {fact}")