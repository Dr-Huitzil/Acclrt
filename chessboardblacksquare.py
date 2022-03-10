col = int(input())
row = int(input())

sum = col - row
even = sum % 2

if (even == 0):
    print("YES")
else:
    print("NO")