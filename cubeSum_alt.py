# Cube sum of first n natural numbers
n = int(input("Enter the number: "))

# Alt A: loop
total = 0
for i in range(1, n + 1):
    total += i ** 3
print("A:", total)

# Alt B: generator expression
print("B:", sum(i ** 3 for i in range(1, n + 1)))

# Alt C: formula (n(n+1)/2)^2
print("C:", (n * (n + 1) // 2) ** 2)
