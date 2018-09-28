"""
Author: Berdal, Ole
Created: 25.09.2018
Edited: 28.09.2018
Version: Python 3.7.0

https://projecteuler.net/problem=2:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
import time
start_time = time.time()


def fib_below(n):
    fib = [1, 2]
    next_fib = fib[-2] + fib[-1]
    while next_fib <= n:
        fib.append(next_fib)
        next_fib = fib[-2] + fib[-1]

    return fib


def remove_odd(numbers):
    return [x for x in numbers if not x % 2]


def main():
    solution = sum(remove_odd(fib_below(4000000)))

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()