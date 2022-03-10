x1 = int(input())
x2 = int(input())
x3 = int(input())

if (x1 < x2 and x1 < x3):
    if x2 < x3:
        n1, n2, n3 = x1, x2, x3
    else: # x2 > x3
        n1, n2, n3 = x1, x3, x2
elif x2 < x1 and x2 < x3:
    if x1 < x3:
        n1, n2, n3 = x2, x1, x3
    else:
        n1, n2, n3 = x2, x3, x1
elif x3 < x1 and x3 < x2:
    if x1 < x2:
        n1, n2, n3 = x3, x1, x2
    else:
        n1, n2, n3 = x3, x2, x1


print(n1)
print(n2)
print(n3)