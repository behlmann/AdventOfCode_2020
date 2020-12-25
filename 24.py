"""Simple script to solve Day 24"""

# === Load input file
from sys import argv, exit
fName = 'input/24.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

fLines = [ll.strip() for ll in fIn.readlines()]

# Hex tiles can be mapped to Cartesian points in Z x Z with different adjacency rules
moveE  = lambda x,z: (x+1      ,z  )
moveW  = lambda x,z: (x-1      ,z  )
moveNE = lambda x,z: (x+(z%2)  ,z+1)
moveSE = lambda x,z: (x+(z%2)  ,z-1)
moveNW = lambda x,z: (x+(z%2)-1,z+1)
moveSW = lambda x,z: (x+(z%2)-1,z-1)
hexMoves = {'e':moveE,'w':moveW,'ne':moveNE,'se':moveSE,'nw':moveNW,'sw':moveSW}

# Use defaultdict to expand to indefinite size and only track the tiles we need
from collections import defaultdict
isBlack = defaultdict(int) # 1 = black, 0 = white (default)
for ll in fLines:
	x,z = 0,0
	hasNS = ''
	for c in ll:
		if c in 'ew':
			# Move on 'e' or 'w'
			fMove = hexMoves[hasNS + c]
			x,z = fMove(x,z)
			hasNS = ''
		elif c in 'ns':
			# Store char and wait for 'e' or 'w'
			hasNS = c
		else:
			print("Unrecognized input:",c)
	colorXZ = isBlack[(x,z)]
	#print("{},{} -> {}".format(x,z,'white' if colorXZ else 'black'))
	# Flip tile
	isBlack[(x,z)] = 0 if colorXZ else 1

print("Part 1:",sum(isBlack.values()))

# Functions for getting the six adjacent tiles
fAdjacent = hexMoves.values()
# Count neighbors with 1 = black
def countNeighbors(x,z):
	neighborBlack = [isBlack[f(x,z)] for f in fAdjacent]
	return sum(neighborBlack)

# Functions used for printing hex grid
symbol = lambda x,z: '#' if isBlack[(x,z)] else '_'
symbolC = lambda x,z: symbol(x,z) if (x or z) else ('0' if isBlack[(x,z)] else 'o')

# Black squares (isBlack) remain what we found in Part 1
nDays = 100
for iDay in range(nDays):
	# Only iterate through the portion of the grid with black (plus margin of 1)
	blackKeys = [k for k in isBlack.keys() if isBlack[k]]
	xVals = [coo[0] for coo in blackKeys]
	zVals = [coo[1] for coo in blackKeys]
	xMin, xMax = min(xVals)-1, max(xVals)+1
	zMin, zMax = min(zVals)-1, max(zVals)+1
	# Used for printing & debugging
	#for z in range(-10,10):
	#	pad = ' ' if z%2 else ''
	#	print(pad + ' '.join([symbolC(x,z) for x in range(-10,10)]))
	
	# Track which tiles need to be flipped colors
	makeBlack = set()
	makeWhite = set()
	for x in range(xMin,xMax+1):
		for z in range(zMin,zMax+1):
			nc = countNeighbors(x,z)
			if isBlack[(x,z)]:
				if nc<1 or nc>2:
					makeWhite.add((x,z))
			else:
				if nc==2:
					makeBlack.add((x,z))
	
	# Flip tiles
	for xz in makeBlack: isBlack[xz] = 1
	for xz in makeWhite: isBlack[xz] = 0
	#if (iDay+1)%10==0:
	#	print("Day {}: {}".format(iDay+1,sum(isBlack.values())))

print("Part 2:",sum(isBlack.values()))