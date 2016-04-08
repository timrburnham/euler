n = 0
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        x = i * j
        if x > n:
            s = str(x)
            if s == s[::-1]: n = x
print n