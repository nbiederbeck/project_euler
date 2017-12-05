'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
from projecteuler.euler0003 import primefactors
from numpy import array


NUMBER = 13195
SOLUTION = array([9, 7, 13, 29])


def test():
    assert primefactors(NUMBER).all() == SOLUTION.all()
