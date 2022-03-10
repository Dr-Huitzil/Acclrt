n = int(input())
max = n

while n != 0:
    n = int(input())
    if n > max:
        max = n
    elif n == 0:
        break
print(max)