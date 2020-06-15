from cs50 import get_float

while True:
    change = get_float("Change owed: ") #get input
    if change >= 0:  #account for invalid input
        break

#after getting input round
q = round(change * 100)
coins = 0

#Quarters
while q >= 25:
        q = q - 25         #-= operator: https://stackoverflow.com/questions/37845445/and-symbols-in-python/37845498
        coins += 1

#Dimes
while q >= 10:
        q = q - 10
        coins += 1

#Nickels
while q >= 5:
        q = q - 5
        coins += 1

#Pennies
while q >= 1:
        q = q - 1
        coins += 1

#print output based on input
print(coins)
