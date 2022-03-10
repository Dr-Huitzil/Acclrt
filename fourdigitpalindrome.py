num = int(input())

num1 = (num % 10**4) // 10**(4-1)
num2 = (num % 10**3) // 10**(3-1)
num3 = (num % 10**2) // 10**(2-1)
num4 = (num % 10**1) // 10**(1-1)

set2 = (num4 * 10) + num3
set1 = (num1 * 10) + num2

if(set1 == set2):
    print("YES")
else:
    print("NO")