"""Simple script to solve Day 13"""

# === Load input file
from sys import argv, exit
fName = 'input/13.txt' if len(argv)<2 else argv[1]
try:
	fIn = open(fName,'r')
except FileNotFoundError:
	print("Error in {}: File {} was not found".format(__file__, fName))
	exit(-1)

# Earliest timestamp you could depart
t0 = int(fIn.readline().strip())
lBus = [x for x in fIn.readline().strip().split(',')]

# === Part 1
# Buses running (Bus # is the same as the interval between trips for that bus)
bRun = [int(x) for x in lBus if x.isnumeric()]
# Waiting times for buses
dt = [(t - t0) % t for t in bRun]
# Minimum waiting time and corresponding bus number
dtMin = min(zip(dt,bRun))
print("Part 1:", dtMin[0] * dtMin[1])

# === Part 2
# This is a Chinese Remainder Theorem problem.
# All bus numbers in the examples are distinct primes, which simplifies the calculation.
bAll = [int(x) if x.isnumeric() else None for x in lBus]
prod = 1
tAns = 0
for i,z in enumerate(bAll):
	if not z: continue # Bus not running
	while (z-tAns) % z != i % z:
		# Add product of primes (AKA bus numbers) so far until the modulus for the
		# new bus number z is correct.
		tAns += prod
	prod *= z
print("Part 2:",tAns)