"""Simple script to solve Day 9"""

# === Load input file
from sys import argv, exit
fName = 'input/09.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

# === Main script
fLines = fIn.readlines()
ser = [int(ll.strip()) for ll in fLines]
nSer = len(ser)

# === Part 1
# Preamble length: Differs for main input and example
nPre = 25 if 'example' not in fName else 5

# Cache sums of element ix with each of the (nPre-1) next elements
sumList = [[]] * nSer
for ix,x in enumerate(ser):
	xSums = [x + ser[ix+di] for di in range(1,min(nPre,nSer-ix))]
	sumList[ix] = xSums

for iz,z in enumerate(ser):
	# Skip preamble
	if iz<nPre: continue
	# Check eligible elements of sumList[iz-di] for a match
	for di in range(2,nPre+1):
		if z in sumList[iz-di][:di-1]:
			break
	else:
		# No match for z => Answer to Part 1
		ans1 = z
		print("Part 1:",z)
		break

# === Part 2
# Search for range of elements ser[iL:iR] that adds to ans1
for iL in range(nSer):
	tot = 0
	iR = iL
	# Accrue until at least equal to ans1
	while tot < ans1 and iR<nSer:
		tot += ser[iR]
		iR += 1
	if tot==ans1:
		xSmall = min(ser[iL:iR])
		xLarge = max(ser[iL:iR])
		print("Part 2:",xSmall+xLarge)
		break
