## Fibannocii series Logic code issue.
a = 1
b = 1
print(a,end= " ")
max = 100
while a < max:
    a,b = b,a+b
    if a < max:
        print(a, end=" ")
    
    