"""Simple script to solve Day 12"""

# === Load input file
from sys import argv, exit
fName = 'input/12.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

fLines = [ll.strip() for ll in fIn.readlines()]
inst = [(x[0],int(x[1:])) for x in fLines]

# Use (x,y) coordinates with: N=+y, S=-y, E=+x, W=-x
dirDict = {'N':(0,1),'S':(0,-1),'E':(1,0),'W':(-1,0)}
# List of headings for the ship, ordered CCW
lHead = [(1,0),(0,1),(-1,0),(0,-1)] # i.e. [N,E,S,W]
# Current heading as an index in lHead
iHead = 0

# === Part 1
# Ship's position
x,y = 0,0
for s,n in inst:
	if s in dirDict:
		x += n * dirDict[s][0]
		y += n * dirDict[s][1]
	elif s=='L':
		if n%90!=0: print("WARNING: Turn angle not divisible by 90 degrees.")
		iHead = (iHead + n//90) % 4
	elif s=='R':
		if n%90!=0: print("WARNING: Turn angle not divisible by 90 degrees.")
		iHead = (iHead - n//90) % 4
	elif s=='F':
		x += n * lHead[iHead][0]
		y += n * lHead[iHead][1]
	else:
		print("ERROR: Instruction not recognized:",s,n)
		exit(-2)

print("Part 1:",abs(x)+abs(y))

# === Part 2
x,y = 0,0
# Waypoint coordinates (relative to ship)
xw, yw = 10, 1

for s,n in inst:
	if s in dirDict:
		xw += n * dirDict[s][0]
		yw += n * dirDict[s][1]
	elif s=='L':
		# Perform left rotation n//90 times
		for r in range(0,n,90):
			xw, yw = -yw, xw
	elif s=='R':
		for r in range(0,n,90):
			xw, yw = yw, -xw
	elif s=='F':
		x += n * xw
		y += n * yw
	else:
		print("ERROR: Instruction not recognized:",s,n)
		exit(-2)

print("Part 2:",abs(x)+abs(y))