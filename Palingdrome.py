#Given number is Palingdrome or not.
number =151
reverse=0
temp =number
while number >0:
    remainder = number % 10
    reverse = (reverse * 10) + remainder
    number =number//10
if temp == reverse:
    print("The number is Palingdrome:")
else:
    print("The number is not a Palingdrome:")   