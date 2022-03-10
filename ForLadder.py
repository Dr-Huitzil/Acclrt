#user solution
for i in range(1, (int(input()))+1):
    print('\n')
for j in range(1, i+1):
    print(j, end='')


#model solution

for i in range(1, (int(input()))+1):
    for j in range(1, i+1):
        print(j, end='')
    print()