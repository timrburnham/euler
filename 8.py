adjac = 4
maxprod = 0
maxstr = '0'

with open('1000.txt') as fil:
	str = fil.read().rstrip('\n ')
	spl = str.split('0')

for seg in spl:
	if len(seg) => adjac:
		for char in seg:
			