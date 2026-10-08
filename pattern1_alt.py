rows = 5

# Alt A: join
print("A:")
for i in range(1, rows + 1):
    print(" ".join(str(j) for j in range(1, i + 1)))

# Alt B: unpack range
print("B:")
for i in range(1, rows + 1):
    print(*range(1, i + 1))

# Alt C: build the row step by step
print("C:")
row = ""
for i in range(1, rows + 1):
    row += f"{i} "
    print(row)
