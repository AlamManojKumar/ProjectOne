max =10
index =0
sum =0
result =0
while index<=max:
    if index %3==0 or index %5==0:
        result =result+index
        index =index+1  
print(result)
