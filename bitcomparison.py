input = int(input())

lst_input = input.split()

def islastbitset(n):
    if(n & 1):
        return 1
    else:
        return 0;

val1 = int(lst_input[0])
n1_lastbit = islastbitset(val1)
val2 = int(lst_input[1])
bin2 = bin(val2)
n2_lastbit = islastbitset(val2)

if (n1_lastbit == n2_lastbit):
    print("True")
else:
    print("False")