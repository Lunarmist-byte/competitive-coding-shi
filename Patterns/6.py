numBottles =int(input())
numExchange =int(input())
total=numBottles
empty=numBottles
while empty>=numExchange:
    new_bottles=empty//numExchange
    total+=new_bottles
    empty=empty%numExchange+new_bottles
print(total)