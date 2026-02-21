#Prime or not 
number = 7
is_prime = True
index = 2
while index < number:
    if number % index == 0:
        is_prime = False
        break
    index += 1

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")


