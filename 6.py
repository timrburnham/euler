def sumsquares(a):
	x = (a * (a + 1)) // 2
	return (x * x)

def squaresums(a):
	return (a * (a + 1) * (2 * a + 1)) // 6

x = 100
print(sumsquares(x) - squaresums(x))