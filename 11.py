"""Simple script to solve Day 10"""

# === Load input file
from sys import argv, exit
fName = 'input/11.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

from copy import deepcopy

fLines = [ll.strip() for ll in fIn.readlines()]
emp='L'
occ='#'
flo='.'
w,h = len(fLines[0]),len(fLines)

hasSeat = [[(0 if fLines[y][x]=='.' else 1) for x in range(w)] for y in range(h)]
print(hasSeat)
taken = [[(1 if fLines[y][x]=='#' else 0) for x in range(w)] for y in range(h)]

def nAdj(taken, x, y):
	ret = 0
	for i in range(max(x-1,0),min(x+2,w)):
		for j in range(max(y-1,0),min(y+2,h)):
			if (i,j)==(x,y): continue
			ret += taken[j][i]
	return ret

def nTotal(taken):
	ret = 0
	for l in taken:
		ret += l.count(1)
	return ret

for r in range(100):
	#nAdj = [[0]*w]*h
	tkUp = deepcopy(taken)
	print(nTotal(taken))
	for x in range(w):
		for y in range(h):
			if not hasSeat[y][x]: continue
			nxy = nAdj(taken,x,y)
			#print(x,y,nxy)
			if taken[y][x] and nxy >= 4: tkUp[y][x] = 0
			if (not taken[y][x]) and nxy == 0: tkUp[y][x] = 1
			#tkUp[y][x] = 1 if ((taken[y][x] and nxy < 4) or (nxy==0 and not taken[y][x])) else 0
	taken = tkUp
	#print(taken)
	
