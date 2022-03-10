year = int(input())

leapyear = year % 400
leap = year % 4
common = year % 100


if(leapyear == 0):
   print("LEAP")
elif(common == 0):
   print("COMMON")
elif (leap == 0):
    print("LEAP")
else:
    print("COMMON")