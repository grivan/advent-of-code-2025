INPUT = open("day3.in")

lines = [l.strip() for l in INPUT.readlines()]

maxes = 0

for line in lines:
    start = 0
    cl = ""
    #print(line)
    for i in range(11, -1, -1):
        test_line = line[start:-i]
        if i == 0:
            test_line = line[start:]
        for j in range(9, 0,-1):
            try:
                s = test_line.index(str(j)) + start
                # print(i, j, test_line, s)
                cl += str(j)
                start = s + 1
                break
            except ValueError:
                continue
    maxes += int(cl)

print(maxes)