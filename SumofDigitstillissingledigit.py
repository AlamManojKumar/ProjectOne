# Sum of Digit till it is single digit
# 5678 => 5+6+7+8 = 18+8 => 26
number =5678
result=0
while number>0:
    rem = number%10
    result = result+rem
    number = number//10
    if number==0 and result>9:
       number = result
       result =0
       end if
end while
print result
