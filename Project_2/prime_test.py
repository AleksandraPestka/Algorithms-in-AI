""" Verify if the number is prime. """

import numpy as np

def is_valid(variable):
    try:
        if variable.isdigit():
            if int(variable) < 0:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print('Provide an integer number >= 0')
        return False

    return True        

def is_prime(variable):
    variable = int(variable)

    if variable < 2:
        return False
    elif variable <= 3:
        return True
    
    if (variable%2 == 0) or (variable%3 == 0):
        return False

    for i in range(5, int(np.sqrt(variable))):
        if variable%i == 0:
            return False
    
    return True

if __name__ == '__main__':
    valid = False
    while not valid:
        var = input("Enter a number to test: ")
        valid = is_valid(var)

    print(f'Is it a prime number? {is_prime(var)}')


