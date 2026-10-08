# NOTE: original compared `num` (always 0 after the loop) with `n`.
# It must compare the reversed number with the original.
num = int(input("Enter the number: "))

# Alt A: fixed version of your loop
rev, temp = 0, num
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("A:", "Palindrome" if rev == num else "Not palindrome")

# Alt B: string slicing
print("B:", "Palindrome" if str(num) == str(num)[::-1] else "Not palindrome")

# Alt C: two pointers
d = str(num)
l, r = 0, len(d) - 1
is_pal = True
while l < r:
    if d[l] != d[r]:
        is_pal = False
        break
    l += 1
    r -= 1
print("C:", "Palindrome" if is_pal else "Not palindrome")
