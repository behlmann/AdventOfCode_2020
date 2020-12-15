"""Simple script to solve Day 14"""

# === Load input file
from sys import argv, exit
fName = 'input/14.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

def intToNBitBinary(x,N):
	# Convert int to binary, remove "0b" prefix, and left pad with zeros to N bits
	return bin(x)[2:].zfill(N)

def decodeMemoryAddress(addrIn, bitmask):
	# Decode memory addresses as in Part 2 of the problem
	sIn = intToNBitBinary(addrIn,36)
	useChar = lambda cIn, cMask: cIn if (cMask=='0') else cMask
	return ''.join([useChar(cIn,cMask) for (cIn,cMask) in zip(sIn,bitmask)])
	
# === Part 1
bitInMask, maskContent = 0, 0
# Dict holds values in memory
mem = dict()

fLines = fIn.readlines()
for ll in fLines:
	if ll[:4]=='mask':
		foo1,foo2,msk = ll.strip().partition(" = ")
		# Split mask into two separate parts, both binary
		sBitInMask   = ''.join(['0' if c=='X' else '1' for c in msk])
		sMaskContent = ''.join(['1' if c=='1' else '0' for c in msk])
		bitInMask    = int(sBitInMask,base=2)
		maskContent  = int(sMaskContent,base=2)
	else:
		sMem,foo2,sVal = ll.strip().partition(' = ')
		# Apply masks using bitwise operations
		val = int(sVal)
		val &= (~bitInMask)
		val |= maskContent
		# Store value to memory address
		iMem = int(sMem[4:-1])
		mem[iMem] = val

ans1 = sum(mem.values())
print("Part 1:",ans1)

# === Part 2
# Current mask
maskNow = None
# Luckily, the number of memory addresses used is small, so we can store all of them
# in a dict as above.  (There is capacity for 2**36 addresses.)
mem2 = dict()
for ll in fLines:
	if ll[:4]=='mask':
		foo1,foo2,maskNow = ll.strip().partition(" = ")
	else:
		sMem,foo2,sVal = ll.strip().partition(' = ')
		nVal = int(sVal)
		iMem = int(sMem[4:-1])
		memToWrite = decodeMemoryAddress(iMem,maskNow)
		nX = memToWrite.count('X')
		if nX==0:
			mem2[int(memToWrite,2)] = nVal
		memTemplate = memToWrite.replace('X','{}')
		# Cycle through all 2**nX possibilities for 'floating' bits
		for z in range(2**nX):
			bitList = intToNBitBinary(z,nX) # bin(z)[2:].zfill(nX)
			memLoc = memTemplate.format(*bitList)
			mem2[int(memLoc,2)] = nVal

print("Part 2:",sum(mem2.values()))
