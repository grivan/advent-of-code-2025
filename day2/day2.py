INPUT = open("day2.in")

inp = INPUT.readlines()
ranges = inp[0].strip()

ranges = [r.split('-') for r in ranges.split(',')]

count = []

for r in ranges:
    s = int(r[0])
    e = int(r[1])
    for n in range(s, e+1):
      ns = str(n)
      nsns = ns + ns
      i = nsns.index(ns, 1) # read https://www.baeldung.com/java-repeated-substring
      if i != len(ns):
         count.append(n)

print(sum(count))