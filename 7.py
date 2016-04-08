import primes, itertools

def nth(iterable, n, default=None):
	"Returns the nth item or a default value"
	return next(itertools.islice(iterable, n, None), default)

n = 10001
print(nth(primes.psieve(), n-1))