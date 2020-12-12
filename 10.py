"""Simple script to solve Day 10"""

# === Load input file
from sys import argv, exit
fName = 'input/10.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

adapters = [int(ll.strip()) for ll in fIn.readlines()]
adapters.sort()
maxJolts = adapters[-1]+3
adapters.append(maxJolts)
nAdapters = len(adapters)

adapters.insert(0,0)

dJolts = [adapters[j+1]-adapters[j] for j in range(nAdapters)]
nd3, nd1 = dJolts.count(3), dJolts.count(1)
print("Part 1:",nd3 * nd1)

print(nAdapters)
print([dJolts.count(x) for x in range(5)])

nRoutes = [0] * (maxJolts+1)
nRoutes[0] = 1
for j in range(1,maxJolts+1):
	if j in adapters:
		jMin = max(0,j-3)
		nRoutes[j] = sum(nRoutes[jMin:j])

print("Part 2:",nRoutes[maxJolts])