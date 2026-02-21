###Palingderome number
number =151
temp=0
rem=0
reverse =0
while number >0:
    rem = number % 10 
    reverse = (reverse *10) + rem
    number = number//10
if temp == reverse:
    print("The number is Palingdrome:")
else:
    print("The number is not Palingdrome:")   
  


