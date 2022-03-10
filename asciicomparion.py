user_input = input()
letter = user_input[len(user_input)-1] 
 
 
tens_place = ((ord(letter) % 10**2) // 10**1) %2
ones_place = (ord(letter)%10)

tens_lsb = tens_place % 2
ones_lsb = ones_place % 2 

if(ones_lsb == tens_lsb): 
    print("Lsb matches:", tens_lsb, ones_lsb) 
else: 
    print("Lsb does not match:", tens_lsb, ones_lsb)