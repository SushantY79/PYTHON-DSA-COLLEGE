num = 125

# Alt A: string + generator
print("A:", sum(int(d) for d in str(num)))

# Alt B: divmod loop
t, total = num, 0
while t:
    t, d = divmod(t, 10)
    total += d
print("B:", total)

# Alt C: recursion
def digit_sum(n):
    return 0 if n == 0 else n % 10 + digit_sum(n // 10)

print("C:", digit_sum(num))
