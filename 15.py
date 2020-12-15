"""Simple script to solve Day 15"""

#=== Load input file
from sys import argv, exit
fName = 'input/15.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

# List of numbers spoken at beginning
listIn = [int(x) for x in fIn.readline().strip().split(',')]
# Answers for Parts 1 & 2 are numbers at these goal indices
iMax1 = 2020
iMax2 = 30000000

# Rather than explicitly storing the whole list, we only need the last time each number
# was said, which can be tracked in a dict (zIndex).
# zIndex[key] = last time the key was said (one-indexed)
zIndex = {z:iz+1 for iz,z in enumerate(listIn[:-1])}
i0 = len(listIn)
# z = next element to be added to dict; zNext follows
z, zNext = None, listIn[-1]
for i in range(i0,iMax2+1):
	z = zNext
	if z in zIndex:
		zNext = i - zIndex[z]
	else:
		zNext = 0
	# Only add z to dict after computing zNext
	zIndex[z] = i
	if (i==iMax1): print("Part 1:",z)
	if (i==iMax2): print("Part 2:",z)