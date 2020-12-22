"""Simple script to solve Day 21"""

# === Load input file
from sys import argv, exit
fName = 'input/21.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

fLines = [ll.strip() for ll in fIn.readlines()]
ingrNumbers = dict()
ingrOrdered = []
nIngr = 0
alrgNumbers = dict()
alrgOrdered = []
nAlrg = 0
si = []
sa = []
for ll in fLines:
	iParenL = len(ll) if ('(contains ' not in ll) else ll.index('(')
	iParenR = ll.find(')',iParenL)
	llIngr = ll[:iParenL].rstrip().split(' ')
	stIngr = set()
	for ingr in llIngr:
		if ingr not in ingrNumbers:
			ingrNumbers[ingr] = nIngr
			ingrOrdered.append(ingr)
			nIngr += 1
		if ingr in stIngr: print("Warning: Duplicate ingredients in one food")
		stIngr.add(ingrNumbers[ingr])
	#if iParenR>iParenL:
	llAlrg = [x.strip() for x in ll[iParenL+10:iParenR].split(',')]
	#else:
	#	llAllergen = []
	stAlrg = set()
	for alrg in llAlrg:
		if alrg not in alrgNumbers:
			alrgNumbers[alrg] = nAlrg
			alrgOrdered.append(alrg)
			nAlrg += 1
		stAlrg.add(alrgNumbers[alrg])
	
	si.append(stIngr)
	sa.append(stAlrg)

ingrRemain = [x for x in range(nIngr)]
alrgRemain = [x for x in range(nAlrg)]
ingrMap = dict()
progress = True
while progress and alrgRemain:
	progress = False
	for al in alrgRemain:
		sIntersect = set(ingrRemain)
		for k,sAl in enumerate(sa):
			if al in sAl:
				sIntersect.intersection_update(si[k])
			if len(sIntersect) == 1:
				progress = True
				ingr = sIntersect.pop()
				alrgRemain.remove(al)
				ingrRemain.remove(ingr)
				ingrMap[alrgOrdered[al]] = ingrOrdered[ingr]
				break

stRem = set(ingrRemain)
tot = 0
for ss in si:
	tot += len(ss.intersection(stRem))
print("Part 1:",tot)

alrgSorted = sorted(alrgOrdered)
ans2 = ','.join([ingrMap[x] for x in alrgSorted])
print("Part 2:",ans2)