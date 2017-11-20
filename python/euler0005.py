'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
# coding: utf-8
import numpy as np


TEST_ARRAY = np.arange(1, 10)
TEST_SOLUTION = 2520
VERIFY_ARRAY = np.arange(1, 20)


# print('Test: 2*3*2*5*7*2*3 = {sol}'.format(sol=2*3*2*5*7*2*3))
# print('Solution: 2*3*2*5*7*2*3*11*13*2*17*19 = {sol}'.format(sol=2*3*2*5*7*2*3*11*13*2*17*19))


def smallest_multiple(array):
    sm = 1
    for number in array:
        for test in array:              #  <----------+
            if number % array != 0:     #             |
                sm *= number            #             |
                break                   # breaks this |
            else:
                sm *= (number / test)
    return sm


if __name__ == '__main__':
    # print(smallest_multiple(TEST_ARRAY))
    if smallest_multiple(TEST_ARRAY) == TEST_SOLUTION:
        print('Calculating ...')
        print('Solution: {sol}'.format(sol=smallest_multiple(VERIFY_ARRAY)))
    else:
        print('Program faulty.')

