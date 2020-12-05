"""Simple script to solve Day 4"""

from sys import argv, exit
fName = 'input/04.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

allFields = {'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'}

# --- Part 1: Function to check single passport
# input d is a dictionary of {'key':'value'} pairs
def checkPassport1(d):
	for fld in allFields:
		if fld not in d and fld!='cid': return 0
	return 1

# --- Part 2: Write validation functions returning 0 or 1 for each field
# Same function for all 3 "year" fields with min and max arguments
def vYear(s,yMin,yMax):
	if not s.isdigit(): return 0
	y = int(s)
	if y<yMin or y>yMax or not y: return 0
	return 1

def vHeight(s):
	if s[-2:]=='in':
		h = int(s[:-2])
		return 0 if (h<59 or h>76) else 1
	elif s[-2:]=='cm':
		h = int(s[:-2])
		return 0 if (h<150 or h>193) else 1
	return 0

def vHair(s):
	if s[0]!='#' or len(s)!=7: return 0
	for c in s[1:]:
		if c not in '0123456789abcdef': return 0
	return 1

eyeColors = {'amb','blu','brn','gry','grn','hzl','oth'}
def vEye(s):
	return 1 if s in eyeColors else 0

def vPID(s):
	return 1 if (len(s)==9 and s.isdigit()) else 0
# ---

def checkPassport2(d):
	# Needs to pass Part 1 criteria and all 7 data validations
	if not checkPassport1(d): return 0
	val = vYear(d['byr'],1920,2002) and vYear(d['iyr'],2010,2020) and vYear(d['eyr'],2020,2030)
	val = val and vHeight(d['hgt']) and vHair(d['hcl']) and vEye(d['ecl']) and vPID(d['pid'])
	return 1 if val else 0


pd = dict()
nValid1 = 0
nValid2 = 0
# Read all lines at once
fLines = fIn.readlines()
for ll in fLines:
	# Blank line -> process passport then clear dict
	if not ll.strip():
		nValid1 += checkPassport1(pd)
		nValid2 += checkPassport2(pd)
		pd.clear()
	else:
		# Parse into dict format
		for ss in ll.strip().split(' '):
			a,b = ss.strip().split(':')
			pd[a]=b

print("Part 1:",nValid1)
print("Part 2:",nValid2)