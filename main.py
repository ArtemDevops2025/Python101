def factorial(n):
    if n < 0:
        return "Negative number."

    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(n=5))
