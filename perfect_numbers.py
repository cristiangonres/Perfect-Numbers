"""Verify aliquot sum"""

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1 or number % 1 != 0:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot = sum([num for num in range(1, number) if number % num == 0])
    if aliquot == number:
        return "perfect"
    if aliquot > number:
        return "abundant"
    return "deficient"
