INPUT = open("day3.in")

lines = [l.strip() for l in INPUT.readlines()]

start = -1
maxes = 0
for line in lines:
    found = None
    # print(line)
    for i in range(9,0,-1):
        try:
            found = line[:-1].index(str(i))
            break
        except ValueError:
            continue
    m = int(line[found] + line[found+1])
    for i in range(found+1, len(line)):
        mi = int(line[found] + line[i])
        if mi > m:
            m = mi
    # print(m)
    maxes += m

print(maxes)