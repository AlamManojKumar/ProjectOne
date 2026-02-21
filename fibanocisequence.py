# Fibonacci Series
sum = 2
a = 1
b = 2

while a + b < 100:
    c = a + b
    if c % 2 == 0:
        sum = sum + c

    a = b
    b = c

print("Fibonacci Sequence", sum)