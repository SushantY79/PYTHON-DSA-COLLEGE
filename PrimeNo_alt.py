import math

# NOTE: original range(2, (num+1)//2) misses the last divisor (4 shows as prime)
# and treats 0 and 1 as prime.

# Alt A: sqrt bound
def is_prime_a(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

# Alt B: all()
def is_prime_b(n):
    return n > 1 and all(n % i for i in range(2, math.isqrt(n) + 1))

# Alt C: 6k +/- 1
def is_prime_c(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input("Enter the number: "))
for f in (is_prime_a, is_prime_b, is_prime_c):
    print(f.__name__, ":", "Prime" if f(num) else "Not prime")
