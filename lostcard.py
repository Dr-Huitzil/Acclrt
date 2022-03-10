#model solution
n = int(input())

cards_sum = 0
for i in range(1, n+1):
    cards_sum += i
for i in range(n-1):
    cards_sum -= int(input())

print(cards_sum)

#user solution

n = int(input())
lista = []

for j in range(1, n):
    card = int(input())
    if card in range(1, n+1):
        lista.append(card)
for i in range(1, n+1):
    if i not in lista:
        print(i)