#!/home/t41654b/bin/python

# Euclid's algorithm
# computes Greatest Common Divisor of 2 integers
def gcd(a, b):
	while b != 0:
		x = b
		b = a % b
		a = x
	return x

# Least Common Multiple
def lcm(a):
	x = 1
	for i in range(2, a + 1):
		x = x * i // gcd(x, i)
	return x

# Recursive GCD
def rgcd(a, b):
	if b == 0: return a
	return rgcd(b, a % b)

# Recursive LCM
def rlcm(a):
	if a == 1: return 1
	x = rlcm(a - 1)
	return a * x // rgcd(a, x)

print(rlcm(10))
print(rlcm(20))