month = int(input())
day = int(input())

if month == 2:
    if day == 28:
        month += 1
        day = 1
    else:
        day += 1
elif month == 12:
    if day == 31:
        month = 1
        day = 1
    else:
        day += 1
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day == 30:
        month += 1
        day = 1
    else:
        day += 1
else:
    if day == 31:
        month += 1
        day = 1
    else:
        day += 1

print(month)
print(day)