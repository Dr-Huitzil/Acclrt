n = int(input())
d = 2

while d <= n:
    if n % d == 0:
        print(d)
        break
    else:
        d += 1