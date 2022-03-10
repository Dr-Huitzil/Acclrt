num = int(input())

binn = bin(num)

digit1 = (bin % 10**1) // 10**(1-1)
digit2 = (bin % 10**2) // 10**(2-1)

print(digit1 + " " + digit2)