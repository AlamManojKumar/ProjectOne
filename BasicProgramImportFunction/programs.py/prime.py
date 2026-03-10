if __name__ == "__main__":
     """
       Checks if the number is prime or not

    Args:
        number (int): number to be checked

    Returns:
        bool: Return True if prime otherwise False
    """
    # get the number from the user
     number = int(input("Enter the number: "))
     index =2
     is_prime = True
     if number >= 2:
        is_prime = True
        while index < number:
            if number % index ==0:
                is_prime = False
                break
            index = index + 1
     if is_prime:
        print("The number is Prime:")
     else:
        print("The number is not Prime:")