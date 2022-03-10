def odd_occurences_of_number(nums):
     

    # Initialize result
    res = 0
    
    # Traverse the array
    for element in nums:
        # XOR with the result
        res = res ^ element
    return res
 

print("%d" % odd_occurences_of_number(nums))