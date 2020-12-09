"""Simple script to solve Day 8"""

# === Load input file
from sys import argv, exit
fName = 'input/08.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)
	
# === Define functions
# Parse string instruction into tuple (a,j):
#   - increment accumulator by a
#   - jump j to next instruction
def getAccJmp(sLine):
	op,sp,sArg = sLine.strip().partition(' ')
	arg = int(sArg)
	acc = arg if op=='acc' else 0
	jmp = arg if op=='jmp' else 1
	return acc,jmp

# Run program of (a,j) instructions defined above until instruction number seen twice.
# Output pointer index and accumulator value at termination.
def runUntilLoop(accJmpSeq):
	# Instruction pointer, accumulator
	i, accum = 0, 0
	iSeen = set()
	# Exit condition 1: Loop found
	while i not in iSeen:
		# Exit condition 2: Pointer outside instruction range
		if i<0 or i>=len(accJmpSeq):
			break
		iSeen.add(i)
		a,j = accJmpSeq[i]
		accum += a
		i += j
	return i,accum

# === Main script

fLines = fIn.readlines()
accJmpSeq = [getAccJmp(ll) for ll in fLines]
i1, accum1 = runUntilLoop(accJmpSeq)
print("Part 1:",accum1)

# k, ln = index, line to consider changing
for k,ln in enumerate(fLines):
	prog2 = list(fLines)
	op = ln[:3]
	# Switch 'nop'<->'jmp' or continue if not one of these
	if op=='nop':   prog2[k] = 'jmp' + ln[3:]
	elif op=='jmp': prog2[k] = 'nop' + ln[3:]
	else: continue
	accJmpSeq2 = [getAccJmp(ll) for ll in prog2]
	i2, accum2 = runUntilLoop(accJmpSeq2)
	if i2==len(accJmpSeq2):
		# Normal termination achieved: Pointer is one past program end.
		print("Part 2:",accum2)
		# If all is correct, only one solution for Part 2 will be printed.
