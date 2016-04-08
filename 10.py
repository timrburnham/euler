import primes, time

start = time.time()
summation = sum(primes.psieve(2000000))
elapsed = (time.time() - start)
print("{} found in {} sec.".format(summation, elapsed))