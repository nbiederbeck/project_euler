'''
In this file every useful function declared on the way to solve the problems
is copied to be imported in other problems.
'''
# coding: utf-8
import numpy as np


def primes(number):
    '''Returns all primes from 1 to number.'''
    prims = np.array([2, 3])
    numbers = np.arange(3, number+1, step=2)
    for number in numbers:
        if sum(number % primes == 0) == 0:
            prims = np.append(prims, number)
    return prims


def dividers(number):
    '''Returns a sorted array of all dividers of number.
    Moduloes number%i and calculates number/i,
    repeats till number/i and i are same.'''
    divs = np.array([1])
    for i in range(2, number+1):
        if number % i == 0 and divs[-1] <= number/i:
            if number/i in divs:
                continue
            elif number/i == i:
                divs = np.append(divs, i)
            else:
                divs = np.append(divs, number/i)
                divs = np.append(divs, i)
    return sorted(divs)
