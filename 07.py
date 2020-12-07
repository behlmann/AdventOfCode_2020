"""Simple script to solve Day 7"""

# === Load input file
from sys import argv, exit
fName = 'input/07.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)
	
# === Parsing functions
# Strip "bag(s)" off end of string; return color
def getColor(sBag):
	iBag = sBag.rfind('bag')
	return sBag[:iBag].strip()

# Return tuple of (# of bags, color) from string
def getNColor(sNBag):
	n,sp,c = sNBag.strip().partition(' ')
	return int(n),getColor(c)

# Parse one line of input
def parseLine(s):
	sL, sR = tuple(ll.split('contain'))
	# Parent bag color
	cL = getColor(sL.strip())
	# List of child bag strings
	lR = [x.strip() for x in sR.split(',')]
	# Special case: "no other bags"
	if len(lR)==1 and lR[0][:2]=='no':
		lR = []
	# List of child bags' (number, color)
	cR = [getNColor(s) for s in lR]
	return cL, cR

# === Main script
from collections import defaultdict
# Store the "child" bags for each color with multiplicity
hasChildren = dict()
# Store the possible "parent" bags for each color
hasParents = defaultdict(list)
for ll in fIn.readlines():
	cParent, ncChildren = parseLine(ll)
	hasChildren[cParent] = ncChildren
	for n,c in ncChildren:
		hasParents[c].append(cParent)

targetBag = 'shiny gold'
# === Part 1: Depth-first search for connected nodes (bags) on child->parent digraph
canHaveTarget = set()
# Start with parents (don't count target bag itself)
bStack = list(hasParents[targetBag])
while bStack:
	b = bStack.pop()
	# Skip if already seen (avoid infinite loop if graph has cycle)
	if b in canHaveTarget: continue
	else:
		canHaveTarget.add(b)
		bStack.extend(hasParents[b])
print("Part 1:",len(canHaveTarget))

# === Part 2: Depth-first search for parent->child digraph, tracking multiplicities
sStack = [(1,targetBag)]
totalBags = -1 # Omit target bag by subtracting one from count
while sStack:
	mult,b = sStack.pop()
	totalBags += mult
	sChildren = [(mult*n,c) for (n,c) in hasChildren[b]]
	sStack.extend(sChildren)
print("Part 2:",totalBags)
