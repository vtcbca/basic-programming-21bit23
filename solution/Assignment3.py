def fibonacci_terms(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example: Generate first 10 Fibonacci numbers
print(fibonacci_terms(10))
