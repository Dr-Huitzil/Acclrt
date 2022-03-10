def plusOne(digits):
    #Set i to length of digits - 1
    i = len(digits) - 1;
    #Initialize a out list
    out = []
    #Calculate temp = digits[i] + 1
    temp = digits[i] + 1
    while(True):
        #If (temp == 10)
        #  Insert 0 on the top of out
        #  Set carry = 1
        #Else
        # Insert temp on the top of out
        # Set carry = 0
        if (temp == 10):
            out.insert(0, 0);
            carry = 1;
        else:
            out.insert(0, temp);
            carry = 0;
        #Decrement i
        i = i - 1;
        #If (i < 0):
        #   Exit from loop
        if (i < 0):
            if (carry == 1):
                out.insert(0,1);
            break;
        #Calculate temp = digits[i] + carry
        temp = digits[i] + carry;
    #Go back to 4
    return out;
input_list = [9, 9, 9, 9]    
output = plusOne(input_list);
print (output);