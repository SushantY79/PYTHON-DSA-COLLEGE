from functools import reduce

array = [12, 22, 12, 32, 44]

# Alt A: built-ins
print("A:", min(array), max(array))

# Alt B: sort, then take the ends
s = sorted(array)
print("B:", s[0], s[-1])

# Alt C: reduce
print("C:", reduce(min, array), reduce(max, array))
