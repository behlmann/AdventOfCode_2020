"""Simple script to solve Day 3"""

from sys import argv, exit
fName = 'input/03.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

def countTrees(treeMap, dx, dy):
	w, h = len(treeMap[0].strip()), len(treeMap)
	x, y = 0, 0
	nTrees = 0
	while y < h:
		if treeMap[y][x] == '#':
			nTrees += 1
		y += dy
		x += dx
		x %= w # Map is periodic in x, so use mod width
	return nTrees

# Read all lines at once
fLines = fIn.readlines()
print("Part 1:",countTrees(fLines,3,1))

dxs = [1,3,5,7,1]
dys = [1,1,1,1,2]
treeProduct = 1
for dx,dy in zip(dxs,dys):
	treeProduct *= countTrees(fLines,dx,dy)
print("Part 2:",treeProduct)