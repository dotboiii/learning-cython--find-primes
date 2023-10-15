import prime_functions_cy  # Import the Cython module
import prime_functions_python
import time

n = 10000  # The number of prime numbers you want to find set to whatever you want, higher numbers will take longer to compute. If you want higher than 10000 in cython you will have to compile it again with a higher number in the setup.py file.

# Measure execution time for Python
start_time = time.time()
prtimes_python = prime_functions_python.find_primes_python(n)
end_time = time.time()
execution_time_python = end_time - start_time
print(f"The first {n} prime numbers found with Python are: {prtimes_python}")
print(f"Execution time for Python: {execution_time_python} seconds")

# Measure execution time for Cython
start_time = time.time()
primes_cython = prime_functions_cy.prime_functions_cy(n)
end_time = time.time()
execution_time_cython = end_time - start_time
print(f"The first {n} prime numbers found with Cython are: {primes_cython}")
print(f"Execution time for Cython: {execution_time_cython} seconds")
