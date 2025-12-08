INPUT = open("day7.in")

lines = [list(line.strip()) for line in INPUT.readlines()]

split = 0
paths = [[0 for _ in range(len(lines[0]))] for _ in lines]
paths[0][lines[0].index('S')] = 1

for i in range(len(lines)-1):
    for j in range(len(lines[i])):
        if lines[i][j] == 'S' or lines[i][j] == '|':
            if lines[i+1][j] == '.':
                lines[i+1][j] = '|'
                paths[i+1][j] += paths[i][j]
            elif lines[i+1][j] == '^':
                split += 1
                lines[i+1][j-1] = '|'
                paths[i+1][j-1] += paths[i][j]
                lines[i+1][j+1] = '|'
                paths[i+1][j+1] += paths[i][j]
            else:
                paths[i+1][j] += paths[i][j]

# print("\n".join(["".join(str(line)) for line in lines]))
# print("\n".join(["".join(str(line)) for line in paths]))
print(split)
print(sum(paths[-1]))