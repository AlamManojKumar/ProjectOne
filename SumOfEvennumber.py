# Sum of even numbers between 1 to 10
min = 1
max = 10
sum = 0
# Loop runs until min becomes greater than 10
while min <= max:
    # check the number is even
    if min % 2 == 0:
        sum = sum + min

    # move to the next number (outside if)
    min = min + 1

# print only once (outside loop)
print(sum)
