## How to Print the largest number in the array
numbers  = [10,20,30,40,50,60,70,80,100]
largest = numbers[0]
# start with the first element
for num in numbers:
    if num >largest:
        largest = num
print(largest)