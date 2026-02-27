## Palingdrome debuger Code.
number = 151
reverse = 0
remainder =0
temp=number
while number > 0:
    remainder = number % 10
    reverse = reverse * 10  + remainder
    number = number // 10
if temp == reverse:
    print("pallendrome")
else:
    print("not a pallendrome")