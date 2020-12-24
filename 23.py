"""Simple script to solve Day 23"""

# === Load input file
from sys import argv, exit
fName = 'input/23.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

sCups = fIn.readline().strip()
lCups0 = [int(c) for c in sCups]
#nMoves = 10
nMoves = 100

# mod N returning values {1,2,...,N}
modN = lambda x,n: x % n if (x%n>0) else n

lCups = list(lCups0)
nCups = len(lCups)
currentCup = lCups[0]
iCurrent = 0
#print(lCups)
for iMove in range(nMoves):
	moveCups = []
	for j in range(3):
		iPop = (lCups.index(currentCup) + 1) % len(lCups)
		moveCups.append(lCups.pop(iPop))
	targetCup = modN(currentCup-1,nCups)
	while targetCup not in lCups:
		targetCup = modN(targetCup - 1,nCups)
	iInsert = lCups.index(targetCup)
	#print(targetCup,moveCups)
	for j in range(3):
		lCups.insert(iInsert+1,moveCups.pop())
	iCurrent = lCups.index(currentCup)+1
	iCurrent %= nCups
	currentCup = lCups[iCurrent]
	#print(lCups,currentCup)
i1 = lCups.index(1)
print("Part 1:",''.join([str(c) for c in lCups[i1+1:] + lCups[:i1]]))
