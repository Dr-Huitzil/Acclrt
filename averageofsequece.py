n = int(input())
sum = n
count = 0

while n != 0:
    n = int(input())
    sum += n
    count += 1
    if n == 0:
        break
print(float(sum/count))