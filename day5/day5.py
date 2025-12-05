INPUT = open('day5.in')

lines = INPUT.readlines()

ranges = []
ing = []
found = 0
for i in range(len(lines)):
    line = lines[i].strip()
    if line == '':
        found = 1
        continue
    if not found:
        r = line.split('-')
        ranges.append([int(x) for x in r])
    else:
        ing.append(int(line))

exists = 0
for i in ing:
    for r in ranges:
        if r[0] <= i <= r[1]:
            exists += 1
            break

total_count = 0
merged = []
ranges.sort(key=lambda x: x[0])
for r in ranges:
    if not merged or merged[-1][1] < r[0]:
        merged.append(r)
    else:
        merged[-1][1] = max(merged[-1][1], r[1])

print(exists, sum([m[1]-m[0]+1 for m in merged]))