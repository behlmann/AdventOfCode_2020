"""Simple script to solve Day 16"""

# === Load input file
from sys import argv, exit
fName = 'input/16.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

# === Separate out sections of input file
fLines = [ll.strip() for ll in fIn.readlines()]
div1 = fLines.index('')
fFields = fLines[:div1]
div2 = fLines.index('',div1+1)
if (div2-div1)!=3 or ('your' not in fLines[div1+1]): print("ERROR: Bad assumption in parsing.")
sMyTicket = fLines[div1+2]
if 'nearby' not in fLines[div2+1]: print("ERROR: Bad assumption in parsing.")
fOtherTickets = fLines[div2+2:]

# === Store ranges allowed for each field
fldRanges = dict()
allRanges  = []
for ll in fFields:
	fld,foo,rng = ll.partition(': ')
	fSplitRange = lambda s: s.partition('-')
	# range() objects will make comparison with "in" easy
	rngList = [range(int(lo),int(hi)+1) for lo,sep,hi in map(fSplitRange,rng.split(' or '))]
	fldRanges[fld] = rngList
	allRanges.extend(rngList)

# === Parse my ticket into ints
myTicket = [int(s) for s in sMyTicket.strip().split(',')]

# === Part 1
validTickets = []
errRate = 0
for tkt in fOtherTickets:
	vals = [int(s) for s in tkt.strip().split(',')]
	validTkt = True
	for val in vals:
		# Whether value is valid for "any" field range
		mayBeValid = any([val in rng for rng in allRanges])
		if not mayBeValid:
			errRate += val
			validTkt = False
	# Store only valid tickets for Part 2
	if validTkt:
		validTickets.append(vals)

print("Part 1:",errRate)

# === Part 2
nFields = len(validTickets[0])
# For each field index k, list the candidate names in this dict
fieldCandidate = dict()
for k in range(len(validTickets[0])):
	fldVals = [tkt[k] for tkt in validTickets]
	fieldCandidate[k] = list()
	for fld,rngList in fldRanges.items():
		# IF valid, all tickets must have field k in any of the possible subranges.
		isValid = all([any([val in rng for rng in rngList]) for val in fldVals])
		if isValid:
			fieldCandidate[k].append(fld)

# Use deduction by weeding field names that only match one index
fieldsFound = dict() # key = index, value = name
progress = True
# Avoid possible infinite loop by only continuing if we match a field each iteration
while progress:
	progress = False
	newlyFound = set()
	nCand = {k:len(cList) for k,cList in fieldCandidate.items()}
	for k,nc in list(nCand.items()):
		# Only one candidate for the name of field k
		if nc==1:
			cnd = fieldCandidate.pop(k)
			fieldsFound[cnd[0]] = k
			progress = True
			newlyFound.add(cnd[0])
		elif nc==0:
			print("ERROR: Field #{} has no eligible names!".format(k))
	# Eliminate anything we matched from other indexes' lists
	for fld in newlyFound:
		for cl in fieldCandidate.values():
			if fld in cl:
				cl.remove(fld)

# See if our deduction was enough to locate all fields beginning "departure"
sBegin = 'departure'
allDepart = {f for f in fldRanges if f.startswith(sBegin)}
if allDepart.issubset(set(fieldsFound)) and len(allDepart)==6:
	prod = 1
	for f in allDepart:
		prod *= myTicket[fieldsFound[f]]
	print("Part 2:",prod)