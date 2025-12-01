INPUT = open("day1.in")

c = [s.strip() for s in INPUT.readlines()]
c = [(s[0], int(s[1:])) for s in c]

dial = 50
ecount = 0
rcount = 0

for s in c:
    q,r = divmod(s[1], 100)
    ecount += q

    if s[0] == 'L':
        if dial and dial - r <= 0:
            ecount += 1
        dial = (dial - r) % 100
    else:
        if dial + r >= 100:
            ecount += 1
        dial = (dial + r) % 100
    
    if dial == 0:
        rcount +=1

print(ecount, rcount)