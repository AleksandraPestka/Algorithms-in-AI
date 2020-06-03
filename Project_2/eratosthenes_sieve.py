''' Find all prime numbers up to any given limit.
Use sieve of Eratosthenes algorithm. '''

import numpy as np
import time

def is_valid(text):
    try:
        if text.isdigit():
            if int(text) <= 1:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print('Provide a valid number!')
        return False

    return True        

def find_all_prime_numbers(n):
    lst = list(range(2, n+1))

    num = 2
    while num <= np.sqrt(int(n)):
        # find all multiples of num 
        multiplicity_lst = [item for item in lst 
                            if (item%num==0 and item!=num)]
        # remove them from list 
        for item in multiplicity_lst:
            if item in lst:
                lst.remove(item)
        num += 1

    return lst 

if __name__ == '__main__':
    print('[INFO] The program finds all prime numbers from 2 through n.')
    
    valid = False
    while not valid:
        var_str = input("Enter a natural number > 1: ")
        valid = is_valid(var_str)

    # convert str to int
    var = int(var_str)

    # results
    start = time.time()
    prime_nums = find_all_prime_numbers(var)
    stop = time.time()

    print(f'All prime numbers from range [2, {var}] are: ')
    print(prime_nums)
    print(f'It takes {(stop-start):.5f} seconds.')
        
