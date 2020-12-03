"""Simple script to solve Day 2"""

from sys import argv, exit
fName = 'input/02.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

nValid1, nValid2 = 0, 0
# Read input line by line
ll = fIn.readline().strip()
while ll:
	# Parse using split and map
	rule, password = tuple(map(str.strip,ll.split(':')))
	nc, c = rule.split(' ')
	minc, maxc = tuple(map(int,nc.split('-')))
	
	# Part One: Count occurrences of character c
	ccount = password.count(c)
	if minc<=ccount and ccount<=maxc: nValid1 += 1
	
	# Part Two: Check both positions using zero-indexing
	cpos1 = (c == password[minc-1])
	cpos2 = (c == password[maxc-1])
	# For booleans, use != for XOR
	if cpos1 != cpos2: nValid2 += 1
	
	ll = fIn.readline().strip()

print("Part 1:",nValid1)
print("Part 2:",nValid2)