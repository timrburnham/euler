def fib():
    x = [0, 1]
    pos = False
    while True: 
        yield x[pos]
        x[pos] = x[0] + x[1]
        pos = not pos

gen = fib()
s = 0
while(True):
    # Add fib term if <=4000000 and even. Sequence follows pattern even, odd, odd
    # because odd+odd=even, odd+even=odd
    # (and even+even=even, but that never happens here)
    x = next(gen)
    if x > 4000000: break
    s += x
    next(gen)
    next(gen)

print s