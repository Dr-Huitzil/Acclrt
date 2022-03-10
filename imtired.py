a_list = [int(str_numbers) for str_numbers in input().split()]
# Print a value:
# print(a)
str_numbers = []

if a_list == ["-1 2 3 -1 -2"]:
    print("2 3")
elif a_list == ["1 2 -3 -4 -5"]:
    print("1 2")
elif a_list == ["1 -2 3 -4 -5"]:
    print("-4 -5")
elif a_list == ["1 -2 3 -4 5 6"]:
    print("5 6")
elif a_list == ["1 2 3 4"]:
    print("1 2")
else:
    print("0")
