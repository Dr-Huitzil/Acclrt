#method to return the reverse of binary equivalent
def integer_to_reverse_binary(integer_value):
  
#base condition
    if integer_value==0:
        return ""
    else:
    #recursive call
        return str(integer_value % 2) + integer_to_reverse_binary(int(integer_value/2))

count = 0

#get user input

user_in = input()
last = user_in.split()

a = int(last[0])
b = int(last[1])
c = int(last[2])
d = int(last[3])
n = int(last[4])

#check if nth bit is 1 or not
bin = integer_to_reverse_binary(a)
if bin[n]=='1':
    count = count+1;
bin = integer_to_reverse_binary(b)
if bin[n]=='1':
    count = count+1;
bin = integer_to_reverse_binary(c)
if bin[n]=='1':
    count = count+1;
bin = integer_to_reverse_binary(d)
if bin[n]=='1':
    count = count+1;

#method calling and display the result
print(count)