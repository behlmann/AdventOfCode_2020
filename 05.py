"""Simple script to solve Day 5"""

from sys import argv, exit
fName = 'input/05.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

# Seat codes are just binary numbers with the transformations: F->0, B->1, L->0, R->1
# Seat ID combines row # and column number in a natural way:
#     ID = nRow * 8 + nCol = "nRow" + "nCol"
transTable = str.maketrans('FBLR','0101')
# Track seats filled for Part 2
maxID = 2**(7+3)
highestID, lowestID = 0, maxID
seatsFilled = [0 for x in range(maxID)]
# Read input line by line
ll = fIn.readline().strip()
while ll:
	#sRow = ll[:7]
	#sCol = ll[-3:]
	#nRow = int(sRow.translate(transTable),2)
	#nCol = int(sCol.translate(transTable),2)
	#seatID = 8*nRow + nCol
	# Equivalent to the above, we can get the ID directly from the binary translation
	seatID = int(ll.translate(transTable),2)
	highestID = max(seatID,highestID)
	lowestID  = min(seatID,lowestID)
	seatsFilled[seatID] = 1
	ll = fIn.readline().strip()

print("Part 1:",highestID)

mySeat = seatsFilled.index(0,lowestID,highestID)
print("Part 2:",mySeat)