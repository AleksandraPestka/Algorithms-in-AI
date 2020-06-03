# Finding prime numbers 

## Primality test 
To check if the provided number (integer >= 0) is prime, run:
``` bash
python prime_test.py
```

Sample outputs:
```bash
Enter a number to test: 137
Is it a prime number? True
```

```bash
Enter a number to test: 256
Is it a prime number? False
```

```bash
Enter a number to test: 2.2
Provide an integer number >= 0
```

## Find all prime numbers
Find all prime numbers up to given range (inclusive) using **Eratosthenes Sievie** algorithm. Run :

``` bash
python eratosthenes_sieve.py
```

Sample outputs:
```bash
[INFO] The program finds all prime numbers from 2 through n.
Enter a natural number > 1: 59
All prime numbers from range [2, 59] are: 
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
```

```bash 
Enter a natural number > 1: -1
Provide a valid number!
```

## Constraints 
The maximal n is 99999 and the runtime for it is 33 seconds. <br>
In comparison for n=100 runtime is 0.00055 sec.

## Time complexity 
Time complexity of the Eratosthenes Sieve algorithm is O(n log(log n)).

## Testing 
The code was tested using unit tests written in Python - check  *test_eratosthenes_sieve.py* script. 

- Validity of user's input was tested by passing values:
['xD', '5.5', '-8', '0']. 

- The correctness of Eratosthenes Sievie implementation was tested by comparing the results with built-in function **sieve.primerange()** from the Python library **sympy** for values: [47, 9999].

<br>All tests were passed without errors. 
