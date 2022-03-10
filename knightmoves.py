col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

up = abs(row2 - row1)
over = abs(col2 - col1)

if(over == 1 and up == 2):
    print("YES")
elif(over == 2 and up == 1):
    print("YES")
else:
    print("NO")