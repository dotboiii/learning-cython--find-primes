def find_primes_python(amount):
    primes = []
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
    return primes