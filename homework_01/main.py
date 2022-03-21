def power_numbers(**args):
    """
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    >>> power_numbers()
    []
    """
    return list(map(lambda x: x * x, args))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(x):
    """
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(17)
    True
    >>> is_prime(9)
    False
    """
    if x > 1:
        for i in range(2, x // 2):
            if x % i == 0:
                return False
        return True
    return False


def filter_numbers(numbers, filter_type):
    """
    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    >>> filter_numbers([1, 17, 88], PRIME)
    [17]
    """

    filters = {
        ODD: lambda x: x % 2 == 1,
        EVEN: lambda x: x % 2 == 0,
        PRIME: is_prime
    }

    return list(filter(filters[filter_type], numbers))
