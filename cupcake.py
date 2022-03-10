A=int(input())
B=int(input())

N=int(input()) # Ask user for the number of cupcakes, and take the input in N variable

cents=(A*100)+B # convert the cost of single cupcake into cents by multiplying dollar(A) by 100 and adding cents(B)
total=cents*N # multiplying the cent cost of single cupcake by N, now we have the cost of N cupcakes in cent

totalDollar=int(total/100) # divide the cost of N cupcakes in cent by 100 to get the totalDollar(quotient)
totalCents=total%100 # perform modulus operation by 100 on the cost of N cupcakes in cent to get totalCents(remainder)

print(str(totalDollar) + str(totalCents)) # print the total cost in dollar and cents for N cupcakes