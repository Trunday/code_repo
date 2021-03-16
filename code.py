from functools import reduce


def factorial(number):
    return reduce(lambda x, y: x * y, range(1, number + 1))


print(factorial(5))
