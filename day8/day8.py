INPUT = open("day8.in")

lines = [[int(t) for t in line.strip().split(',')] for line in INPUT.readlines()]

dist = []

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        l1 = lines[i]
        l2 = lines[j]
        t = [(l1,l2), (l1[0] - l2[0])**2 + (l1[1] - l2[1])**2 + (l1[2] - l2[2])**2]
        dist.append(t)

dist.sort(key=lambda x: x[1])

adjlist = []
for i in range(1000): # 5266, 5267
    if i == 5266:
        print("yayy")
    p,d = dist[i]
    adjlist.append([p[0], p[1]])

graphs = {tuple(line):set() for line in lines}

for a in adjlist:
    graphs[tuple(a[0])].add(tuple(a[1]))
    graphs[tuple(a[1])].add(tuple(a[0]))

def visit_rec(node, visited):
    if node in visited:
        return
    visited.add(node)
    neighbors = graphs[node]
    for n in neighbors:
        visit_rec(n, visited)

def dfs():
    visited = set()
    counts = []
    prev = 0
    for g in graphs.keys():
        if g not in visited:
            visit_rec(g, visited)
            counts.append((len(visited) - prev))
            prev = len(visited)
        
    return counts

res = dfs()
res.sort()
r = 1
for i in res[-3:]:
    r*=i

for i in range(5000, 5100):
    print(i, dist[i][0][0][0]*dist[i][0][1][0])

print(r)

# 9617397716