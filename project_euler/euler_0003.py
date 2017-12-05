'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
# coding: utf-8
from numpy import array, append, arange, unique


NUMBER_OF_INTEREST = 600851475143
NUMBER_TEST = 13195
SOLUTION_TEST = array([9, 7, 13, 29])


def primes(maxNumber):
    '''Returns all primes from 1 to maxNumber.'''
    primes = array([2, 3])
    numbers = arange(3, maxNumber+1, step=2)
    for number in numbers:
        if sum(number % primes == 0) == 0:
            primes = append(primes, number)
    return primes


def dividers(number):
    '''Returns a sorted array of all dividers of number.
    Moduloes number%i and calculates number/i,
    repeats till number/i and i are same.'''
    divs = array([1])
    for i in range(2, number+1):
        if number % i == 0 and divs[-1] <= number/i:
            if number/i in divs:
                continue
            elif number/i == i:
                divs = append(divs, i)
            else:
                divs = append(divs, number/i)
                divs = append(divs, i)
    return sorted(divs)


# THIS WORKS TOO, BUT ONLY WITH NUMBERS SMALLER 1e9
# def dividers(number):
#     '''Returns all dividers of number.'''
#     if number >= 1e8:
#         return '{number} is too big.'.format(number=number)
#     possible_dividers = arange(1, int(number/2)+1)
#     dividers = possible_dividers[number % possible_dividers == 0]
#     if len(dividers) == 0:
#         return 'Prime!' # Catch if number is already prime.
#     return dividers


def primefactors(number):
    '''Calculates primeefactors.
    Returns primefactors and all primes used for calculation of the number.'''
    primefactors = array([])
    i = 2
    while True:
        if number % i == 0:
            primefactors = append(primefactors, i)
            number = number/i
            i = 2
            if number <= i:
                break
        else:
            i += 1
    return unique(primefactors)


def main():
    '''Starts the program.'''
    solution = primefactors(NUMBER_OF_INTEREST)
    answer = 'Prime factors of {number} are: {solution}'.format(
            number=NUMBER_OF_INTEREST,
            solution=solution,
            )
    print(answer)


if __name__ == '__main__':
    main()
