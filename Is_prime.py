def get_is_prime(number:int)->list:
   factors = find_factors(number)
   result = []
   for factor in factors:
        if get_is_prime(factors):
           result.append(factor)
        return result
   
  