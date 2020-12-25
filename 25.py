"""Simple script to solve Day 25, Part 1"""

# === Load input file
from sys import argv, exit
fName = 'input/25.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

fLines = [ll.strip() for ll in fIn.readlines()]
kPublicCard = int(fLines[0])
kPublicDoor = int(fLines[1])

modulus = 20201227
subjectNumber = 7

def findLoopSize(publicKey, subjectNumber, modulus):
	x = 1
	iLoop = 0
	while x!=publicKey and iLoop < modulus:
		x *= subjectNumber
		x %= modulus
		iLoop += 1
	if iLoop==modulus:
		print("Error: Iteration limit reached!")
	return iLoop

def applyTransform(nTimes, subjectNumber, modulus):
	x = 1
	for j in range(nTimes):
		x *= subjectNumber
		x %= modulus
	return x

nLoopCard = findLoopSize(kPublicCard, subjectNumber, modulus)
nLoopDoor = findLoopSize(kPublicDoor, subjectNumber, modulus)
print(nLoopCard,nLoopDoor)
kEncryption = applyTransform(nLoopDoor,kPublicCard,modulus)
print("Part 1:",kEncryption)