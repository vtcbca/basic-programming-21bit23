n = int(input("Enter the number of lines: "))

for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")
    # Print numbers
    for j in range(1, 2 * i):
        print(j, end=" ")
    print()
