def pattern_alphabets(n):
    for i in range(n):
        spaces = " " * (n - i - 1) * 4
        print(spaces, end="")
        for j in range(i + 1):
            print(chr(65 + j), end="   ")
        for j in range(i - 1, -1, -1):
            print(chr(65 + j), end="   ")
        print()

# Example usage
pattern_alphabets(5)
