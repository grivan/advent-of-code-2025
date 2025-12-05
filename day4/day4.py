INPUT = open("day4.in")

paper = INPUT.readlines()

paper = [[1 if x == '@' else 0 for x in p.strip()] for p in paper]

ns = [(0,-1),(0,1),(-1,-1),(-1,0),(-1,1),(1,1),(1,-1),(1,0)]

def remove():
    count = 0
    rem = []
    for i in range(len(paper)):
        for j in range(len(paper[0])):
            if paper[i][j] == 0:
                continue
            c = 0
            for n in ns:
                ni = i + n[0]
                nj = j + n[1]
                if ni < 0 or ni >= len(paper):
                    continue
                if nj < 0 or nj >= len(paper[0]):
                    continue
                if paper[ni][nj] == 1:
                    c += 1
            if c < 4:
                rem.append((i,j))
                count += 1
    return count, rem

last = -1
total = 0
while(True):
    if last == 0:
        break
    last, rem = remove()
    total += last
    for r in rem:
        paper[r[0]][r[1]] = 0
print(total)