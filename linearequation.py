a = int(input())
b = int(input())

if (a == b):
    x = "many solutions"
elif (a == 0):
    x = "no solution"
elif (float(b / a)) % 1 != 0:
    x = "no solution"
else:
    x = int(float(b / a))

print(x)