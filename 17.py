"""Script with 3D and 4D cellular automaton classes to solve Day 17"""

import numpy as np

class automaton3D:
	'''3D grid of on/off squares that is updated and expanded at each step after an
	initial state based on rules about the states of surrounding squares.'''
	
	def __init__(self, shape, state0=None):
		if len(shape)!=3:
			print("Error in automaton3D: Must be 3-dimensional.")
		self.dims = shape
		self.grid = np.zeros(self.dims)
		if state0:
			# Pad 2D input to slice in 3D
			grid0 = np.array([state0])
			if grid0.shape == self.dims:
				self.grid = grid0
			else:
				print("Error in automaton3D: Bad dimension on state0.")
		self.nSteps = 0
	
	def step(self):
		gz,gy,gx = self.grid.shape
		newShape = (gz+2,gy+2,gx+2)
		nAdj = np.zeros(newShape)
		# Count how many of each square's neighbors are occupied, including itself
		for dz in range(3):
			for dy in range(3):
				for dx in range(3):
					nAdj[dz:(dz+gz),dy:(dy+gy),dx:(dx+gx)] += self.grid
		# Pad current grid with one row of zeros on each side so active area can expand
		nPad = ((1,1),(1,1),(1,1))
		newGrid = np.pad(self.grid,nPad,'constant')
		for z in range(newGrid.shape[0]):
			for y in range(newGrid.shape[1]):
				for x in range(newGrid.shape[2]):
					cnt = nAdj[z,y,x]
					if newGrid[z,y,x] and (cnt<3 or cnt>4):
						# Turn off square
						newGrid[z,y,x] = 0
					elif cnt==3 and not newGrid[z,y,x]:
						# Ture on square 
						newGrid[z,y,x] = 1
		self.grid = newGrid
		self.nSteps += 1
	
	def countOn(self):
		return np.sum(self.grid)

class automaton4D:
	'''4D grid of on/off squares that is updated and expanded at each step after an
	initial state based on rules about the states of surrounding squares.'''
	
	def __init__(self, shape, state0=None):
		if len(shape)!=4:
			print("Error in automaton4D: Must be 4-dimensional.")
		self.dims = shape
		self.grid = np.zeros(self.dims)
		if state0:
			# Pad 2D input to slice in 4D
			grid0 = np.array([[state0]])
			if grid0.shape == self.dims:
				self.grid = grid0
			else:
				print("Error in automaton4D: Bad dimension on state0.")
		self.nSteps = 0
	
	def step(self):
		gw,gz,gy,gx = self.grid.shape
		newShape = (gw+2,gz+2,gy+2,gx+2)
		nAdj = np.zeros(newShape)
		# Count how many of each square's neighbors are occupied, including itself
		for dw in range(3):
			for dz in range(3):
				for dy in range(3):
					for dx in range(3):
						nAdj[dw:(dw+gw),dz:(dz+gz),dy:(dy+gy),dx:(dx+gx)] += self.grid
		# Pad current grid with one row of zeros on each side so active area can expand
		nPad = ((1,1),(1,1),(1,1),(1,1))
		newGrid = np.pad(self.grid,nPad,'constant')
		for w in range(newGrid.shape[0]):
			for z in range(newGrid.shape[1]):
				for y in range(newGrid.shape[2]):
					for x in range(newGrid.shape[3]):
						cnt = nAdj[w,z,y,x]
						if newGrid[w,z,y,x] and (cnt<3 or cnt>4):
							# Turn off square
							newGrid[w,z,y,x] = 0
						elif cnt==3 and not newGrid[w,z,y,x]:
							# Turn on square
							newGrid[w,z,y,x] = 1
		self.grid = newGrid
		self.nSteps += 1
	
	def countOn(self):
		return np.sum(self.grid)


if __name__=="__main__":
	# === Load input file
	from sys import argv, exit
	fName = 'input/17.txt' if len(argv)<2 else argv[1]
	try:
		fIn = open(fName,'r')
	except FileNotFoundError:
		print("Error in {}: File {} was not found".format(__file__, fName))
		exit(-1)
	
	# Parse input to 0/1 (off/on) 2-dimensional grid
	fLines = [ll.strip() for ll in fIn.readlines()]
	w,l = len(fLines[0]),len(fLines)
	isOn0 = [[(1 if fLines[y][x]=='#' else 0) for x in range(w)] for y in range(l)]
	
	# Step 1: Run 3D automaton for 6 steps
	auto3d = automaton3D((1,w,l),isOn0)
	#print("{} : {}".format(0,auto3d.countOn()))
	for j in range(1,7):
		auto3d.step()
		#print("{} : {}".format(j,auto3d.countOn()))
	print("Step 1:",auto3d.countOn())
	
	# Step 2: Run 4D automaton for 6 steps
	auto4d = automaton4D((1,1,w,l),isOn0)
	#print("{} : {}".format(0,auto4d.countOn()))
	for j in range(1,7):
		auto4d.step()
		#print("{} : {}".format(j,auto4d.countOn()))
	print("Step 2:",auto4d.countOn())