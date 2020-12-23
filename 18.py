"""Simple script to solve Day 18"""

# === Load input file
from sys import argv, exit
fName = 'input/18.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

# === Function Definitions
# Assume that expressions are well formed. This functions handles:
#  - White space (ignored)
#  - Integers
#  - Matched sets of parentheses (...)
#  - Operations + and *
# It returns a list of tokens, where each parenthetical operation becomes a nested list.
def parseExp(s):
	i = 0
	expList = []
	while i<len(s):
		#print(i)
		if s[i].isspace():
			i += 1
		elif s[i].isnumeric():
			iL = i
			i += 1
			while i<len(s) and s[i].isnumeric(): i+= 1
			expList.append(int(s[iL:i]))
		elif s[i] == '(':
			iL = i+1
			iR = i+1
			# Find matching closed parenthesis (pLevel = 0)
			pLevel = 1
			while pLevel>0 and iR<len(s):
				if s[iR]=='(': pLevel += 1
				elif s[iR]==')': pLevel -= 1
				iR += 1
			# Parentheses: Use recursion and make next item a nested list
			expList.append(parseExp(s[iL:iR-1]))
			i = iR + 1
		elif s[i] in '+*':
			expList.append(s[i])
			i += 1
		else:
			print("Ignoring unrecognized symbol:",s[i])
			print('{} "{}"'.format(i,s))
			i += 1
	return expList

# Take the output of parseExp() and add more nesting to enforce precedence of '+' over '*'
def orderOperations(expList):
	# Private function: Descend into list items recursively.
	def recur(tok):
		if type(tok) is list:
			return orderOperations(tok)
		return tok
	# Return as a new list instead of modifying input
	newList = []
	i = 0
	while i<len(expList):
		tok = expList[i]
		# We only need to order '+' operations before '*'
		if (tok=='+') and ('*' in expList) and (len(expList)>3):
			exprL = newList.pop()
			# Do nesting
			newList.append([exprL,tok,recur(expList[i+1])])
			i += 2
		else:
			newList.append(recur(tok))
			i += 1
	return newList

# Evaluate list expression (with nesting) left to right
def evalExpList(expList):
	l = expList.copy()
	while len(l)>2:
		x1 = l.pop(0)
		op = l.pop(0)
		x2 = l[0]
		if type(x1) is list: x1 = evalExpList(x1)
		if type(x2) is list: x2 = evalExpList(x2)
		if op=='+': l[0] = x1 + x2
		elif op=='*': l[0] = x1 * x2
		else: print("Error: Unrecognized operation",op)
	if len(l)==1: return l[0]
	else:
		print("Error: Unrecognized expression",l)
		return None

# === Main script
fLines = fIn.readlines()
ans1 = 0
ans2 = 0
for ll in fLines:
	lExp = parseExp(ll)
	ans1 += evalExpList(lExp)
	lExp2 = orderOperations(lExp)
	ans2 += evalExpList(lExp2)
print("Part 1:",ans1)
print("Part 2:",ans2)