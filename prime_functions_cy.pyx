def prime_functions_cy(int amount):
    cdef int number, x, found
    primes = []
    
    amount = min(amount, 10000)
    
    found = 0
    number = 2
    while found < amount:
        for x in primes:
            if number % x == 0:
                break
        else:
            primes.append(number)
            found += 1
        number += 1
    return_list = [p for p in primes]
    return return_list
