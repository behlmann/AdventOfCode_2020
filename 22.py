"""Simple script to solve Day 22"""

# === Load input file
from sys import argv, exit
fName = 'input/22.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

fLines = [ll.strip() for ll in fIn.readlines()]
sep = fLines.index('')
# Read in starting decks
p1 = [int(ll) for ll in fLines[1:sep]]
p2 = [int(ll) for ll in fLines[sep+2:]]
# Make copies for Part 2
p1b = p1.copy()
p2b = p2.copy()

# === Part 1
nRounds = 0
while p1 and p2:
	nRounds += 1
	c1 = p1.pop(0)
	c2 = p2.pop(0)
	if c1 > c2:
		p1.append(c1)
		p1.append(c2)
	else:
		p2.append(c2)
		p2.append(c1)

deckWinner = p1 if p1 else p2
score1 = sum([x * deckWinner[-x] for x in range(1,len(deckWinner)+1)])
print("Part 1: {} ({} rounds)".format(score1,nRounds))

# === Part 2
# Implement "Recursive Combat" as a recursive function.
# Return winner of this Game (1 or 2) and his deck. The latter is used to calculate the
# final score.
def playRecursive(p1,p2):
	# Store previously seen configurations as a (hashable) tuple in a set
	seen = set()
	# Combine decks into one tuple with a separator
	deckComb = lambda l1,l2: tuple(l1 + [-1] + l2)
	isSeen = lambda l1,l2: deckComb(l1,l2) in seen
	# Failsafe against infinite iteration: Quit and warn after 10000 rounds
	nRounds = 0
	while p1 and p2 and nRounds < 10000:
		if isSeen(p1,p2): return (1,p1)
		seen.add(deckComb(p1,p2))
		nRounds += 1
		c1 = p1.pop(0)
		c2 = p2.pop(0)
		winner = 0 # 0 = not decided yet
		if len(p1) >= c1 and len(p2) >= c2:
			# We need to go deeper... recurse!
			winner,wDeck = playRecursive(list(p1[:c1]),list(p2[:c2]))
		if (winner==0 and c1 > c2) or winner==1:
			# P1 wins round
			p1.append(c1)
			p1.append(c2)
		else:
			# P2 wins round
			p2.append(c2)
			p2.append(c1)
	if nRounds == 10000: print("Too many rounds!")
	return (1,p1) if p1 else (2,p2)

winner,deckWinner = playRecursive(p1b,p2b)
score2 = sum([x * deckWinner[-x] for x in range(1,len(deckWinner)+1)])
print("Part 2:",score2)