def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Print the first 8 numbers of the sequence
terms = 8

for i in range(terms):
    print(fibonacci(i), end=" ")