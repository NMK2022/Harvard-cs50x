from cs50 import get_int


while True:
    height = get_int("Enter block  between 1 and 8: ") #get input
    if height > 0 and height < 9: #set condition on input
        break                       #reject value that is out of range

#print hashes
for h in range(height):
    print(" " * (height - 1 - h), end="")
    print('#' * (h + 1))