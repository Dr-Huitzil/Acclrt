col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

if (abs(col2 - col1) <= 1 and abs(row2 - row1) <= 1):
    print("YES")
else:
    print("NO")