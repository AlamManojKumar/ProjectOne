###Palingderome number
number =151
temp=number
remainder=0
reverse =0
while number >0:
    remainder = number % 10 
    reverse = (reverse *10) + remainder
    number = number//10
if temp == reverse:
    print("The number is Palingdrome:")
else:
    print("The number is not Palingdrome:")   
  


