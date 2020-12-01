"""Simple script to solve Day 1"""

from sys import argv
fIn = open('input/01.txt' if len(argv)<2 else argv[1],'r')

# Use set for entries, dict for {(sums of 2 entries):(first entry)}
ents = set()
sums = dict()

# Read input line by line
ll = fIn.readline().strip()
while ll:
	# Assume integers
	x = int(ll)
	# Loop through previous entries; store sums
	for y in ents:
		sums[x+y] = y
	# If we already saw (2020-x), we have the solution
	xComp = 2020 - x
	if xComp in ents:
		print("Part 1: {:10} = {} * {}".format(x*xComp, x, xComp))
	if xComp in sums:
		m1, m2 = sums[xComp], xComp - sums[xComp]
		print("Part 2: {:10} = {} * {} * {}".format(x*m1*m2, m1, m2, x))
	# Store current entry and read next line
	ents.add(x)
	ll = fIn.readline().strip()
