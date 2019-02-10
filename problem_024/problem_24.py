"""
Author: Berdal, Ole
Created: 09.02.2019
Edited: 10.02.2019
Version: Python 3.6.7

https://projecteuler.net/problem=24:
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import time
start_time = time.time()


def nth_lexicographic_permutation(n, object):
    objects = sorted(list(object))

    return get_lexicographic_n(n - 1, objects) if objects and get_permutations(objects) >= n > 0 else -1


def get_lexicographic_n(n, objects):
    if n == 0:
        return ''.join(map(str, objects))

    for x in range(len(set(objects))):
        permutations = get_permutations(objects[:objects.index(sorted(list(set(objects)))[x])] + objects[objects.index(sorted(list(set(objects)))[x]) + 1:])
        if n < permutations:
            break
        n -= permutations

    return objects.pop(objects.index(sorted(list(set(objects)))[x])) + get_lexicographic_n(n, sorted(objects))


def get_permutations(objects):
    permutations = factorial(len(objects))

    atoms = {}
    for o in objects:
        if o not in atoms:
            atoms[o] = 1
        else:
            atoms[o] += 1
            permutations //= atoms[o]

    return permutations


def factorial(number):
    product = 1
    for n in range(number, 1, -1):
        product *= n
    return product


def main():
    solution = nth_lexicographic_permutation(1000000, "0123456789")

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()