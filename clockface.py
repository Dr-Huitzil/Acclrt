# Statement
# The hour hand of an analog clock turned α degrees since the midnight. Determine the angle by which the minute hand turned since the start of the current hour. Input and output in this problems are integers.

# Example input
# 190  30 31 5 0
# (6:20)

# Example output
# 120
# (20 min)
import math

min=input("Insert hour in degrees =")
result=(float(12)*float(min))/(360)
# print("sd",result)
r=int(min)-180
rule=int(min)%30*12
print(rule)
# if(int(min)%2==0):
#   print
# elif r==0:
#   print(result)
# elif(r>0):
#   t=int((360*r*(2/5))/12)
#   print("2",r,t)
# elif(r<0 and result!=1 and result<1):
#   print((int(min)*12))
# elif(r<0 and result!=1):
#   y=(int(min)*12)/360
#   i,d=divmod(y,1)
#   I=int(i)
#   D=int(d*60)
#   list1=[]
#   id=f"{I}{D}".format(*list1)
#   print("3",I,D,id)
# elif(result==1):
#   print("dd",int(result))

# mins=[]
# for amin in min:
#   mins.append(int(amin))
#   print("amin",amin)

# modResult=math.modf(result)
# print(modResult)
# for mod in modResult:
#   digit=float(mod)
#   t=str(f"{mod}".format(*modResult)).split('.')
#   print("mod",digit,t,(digit%mod))
#   if digit%mod==0:
#     print(round(mod*60))
#     if type(mod) == int : print ("This number is an int")
#     elif type(mod) == float : print ("This number is a float")
# theResult=f"{mins}".format(*mins)
# print("theResult",theResult)

# min2=[]

# for min1 in modResult:
#   min2.append(float(min1))
#   print(min2,min1)
# t=str(f"{min2}".format(*min)).split('.')
# print("result",result,t)

