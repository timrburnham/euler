x = 600851475143
i = 2
while i * i < x:
    while x % i == 0:
        x = x / i
    i += 1
print x