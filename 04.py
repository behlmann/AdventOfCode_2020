"""Simple script to solve Day 4"""

from sys import argv, exit
fName = 'input/04.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

reqd = {'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'}
ecls = {'amb','blu','brn','gry','grn','hzl','oth'}

def checkPassport(kvDict):
	for fld in reqd:
		if fld not in kvDict and fld!='cid': return 0
	return 1

def vYear(s,yMin,yMax):
	if not s.isdigit(): return 0
	y = int(s)
	if y<yMin or y>yMax or not y: return 0
	return 1

def vHeight(s):
	if s[-2:]=='in':
		h = int(s[:-2])
		if h<59 or h>76: return 0
		return 1
	elif s[-2:]=='cm':
		h = int(s[:-2])
		if h<150 or h>193: return 0
		return 1
	return 0

def vHair(s):
	if s[0]!='#' or len(s)!=7: return 0
	for c in s[1:]:
		if c not in '0123456789abcdef': return 0
	return 1

def vEye(s):
	return 1 if s in ecls else 0

def vPID(s):
	if len(s)==9 and s.isdigit(): return 1
	return 0

def checkPassport2(d):
	for fld in reqd:
		if fld not in d and fld!='cid': return 0
	val = vYear(d['byr'],1920,2002) and vYear(d['iyr'],2010,2020) and vYear(d['eyr'],2020,2030)
	val = val and vHeight(d['hgt']) and vHair(d['hcl']) and vEye(d['ecl']) and vPID(d['pid'])
	return 1 if val else 0

# Read all lines at once
fLines = fIn.readlines()
pd = dict()
nValid = 0
nValid2 = 0
for ll in fLines:
	if not ll.strip():
		nValid += checkPassport(pd)
		nValid2 += checkPassport2(pd)
		pd = dict()
	else:
		for ss in ll.strip().split(' '):
			a,b = ss.strip().split(':')
			pd[a]=b

print("Part 1:",nValid)
print("Part 2:",nValid2)