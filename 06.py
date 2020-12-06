"""Simple script to solve Day 6"""

from sys import argv, exit
fName = 'input/06.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

groupAny = set() # Collect letters with ANY "yes" in group
allLetters = {chr(x) for x in range(ord('a'),ord('z')+1)}
groupAll = set(allLetters) # Only retain letters with ALL "yes"
tot1 = 0
tot2 = 0
for ll in (fIn.readlines() + ['']): # Blank line at end to process last group
	if not ll.strip():
		# Add counts to total and reset sets
		tot1 += len(groupAny)
		tot2 += len(groupAll)
		groupAny = set()
		groupAll = set(allLetters)
	else:
		# Set operations make things tidy!
		llSet = set(ll.strip())
		groupAny.update(llSet)
		groupAll.intersection_update(llSet)

print("Part 1:",tot1)
print("Part 2:",tot2)