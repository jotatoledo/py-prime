__OFFSET = 1


def sundaram_sieve(limit: int):
    """Returnes a generator of prime numbers between [1,limit] (both boundaries inclusive)

    Keyword arguments:
    limit -- a positive upper boundary for the generator interval
    """
    if(limit < 0):
        raise ValueError(
            "The value of `limit` can not be negative. Given `{limit}`")
    if(limit < 2):
        return []

    sieveLimit = __generate_limit(limit)
    candidates = [True for candidate in range(1, sieveLimit + 1)]

    for outer in range(1, sieveLimit + 1):
        inner = outer
        while(__sieve_factor(inner, outer) <= sieveLimit):
            candidates[__sieve_factor(inner, outer)-1] = False
            inner += 1

    if(limit >= 2):
        # The prime 2 isnt included in the result, so we need to "push it" into the generator
        yield 2
    for candidate in enumerate(candidates):
        if candidate[1]:
            yield __generate_prime(candidate[0] + __OFFSET)


def __sieve_factor(i: int, j: int):
    return i + j + 2*i*j


def __generate_prime(index: int):
    return index*2 + 1


def __generate_limit(limit: int):
    '''
    In general Sieve of Sundaram, produces primes smaller than 
    (2*x + 2) for a number given number x. Since we want primes 
    smaller than n, we reduce n-2 to half
    '''
    return round((limit-2)/2+.49)
