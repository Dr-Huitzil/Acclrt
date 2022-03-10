n =  int(input())
count = 0

for i in range(n):
    if int(input()) == 0:
        count += 1
    else:
        count += 0
print(count)