import turtle, time, math, random, sys, copy

if (len(sys.argv)<6):
	print("not enough arguments")
	print("Cities, Population, Selection, Mutation, Generation")
	sys.exit()

argCities = int(sys.argv[1])
argPopulation = int(sys.argv[2])
Selection = int(sys.argv[3])
argMutation = int(sys.argv[4])
argGeneration = int(sys.argv[5])
Cities = []
Population = []
Generation = 0

#City generation
def initialSetup():
	for x in range(argCities):
		city = [random.randint(0,200), random.randint(0,200), x+1]
		Cities.append(city)
		print("city "+ str(city[2]) + "	[" + str(city[0]) + ", " + str(city[1])+"]")

	for x in range(argPopulation):
		solution = []
		citysol = Cities[:]
		for x in range(len(Cities)):
			integer = random.randint(0,len(citysol)-1)
			solution.append(citysol[integer])
			citysol.pop(integer)
		print(solution)
		Population.append(Solution(solution))	

def calculateFitness():
	for x in range(len(Population)):	
		Population[x].calcfitness()
	Population.sort(key=lambda X: X.fitness, reverse=False)
	#for x in range(len(Population)):
		#print(Population[x].fitness)
		
def select():
	Selected = []
	for x in range(len(Population)):
		Chosen = False
		k = 0
		while (Chosen == False):
			k += 1
			if (random.randint(1,100) <= Selection):
				Chosen = True
			if (k == len(Population)):
				Chosen = True
		#print(k)
		Selected.append(copy.deepcopy(Population[k-1]))
	return Selected
	
def crossover(sol1, sol2):
	select = random.randint(0,len(sol1.solution)-2)
	solution = []
	solution.append(sol1.solution[select])
	solution.append(sol1.solution[select+1])
	for x in range(len(sol2.solution)):
		notchosen = True
		for k in range(len(solution)):
			if (sol2.solution[x][2] == solution[k][2]):
				notchosen = False
		if (notchosen):
			solution.append(sol2.solution[x])
	return solution
	
def Generatenewpop(Selected):
	NewPop = []
	for x in range(len(Selected)):
		NewPop.append(Solution(crossover(Selected[random.randint(0,len(Selected)-1)],Selected[random.randint(0,len(Selected)-1)])))
		NewPop[x].Mutate()
	return NewPop
	
def newGeneration():
	calculateFitness()
	Selected = select()
	return Generatenewpop(Selected)
	
class Solution():
	def __init__(self, solution):
		self.solution = solution
		self.fitness = 0
	
	def calcfitness(self):
		self.fitness = 0
		for x in range(len(self.solution)-1):
			self.fitness += abs(math.sqrt(math.pow(self.solution[x+1][0]-self.solution[x][0],2)+math.pow(self.solution[x+1][1]-self.solution[x][1],2)))
		self.fitness += abs(math.sqrt(math.pow(self.solution[0][0]-self.solution[len(self.solution)-1][0],2)+math.pow(self.solution[0][1]-self.solution[len(self.solution)-1][1],2)))
	def Mutate(self):
		if (random.randint(1,100) <= argMutation):
			select = random.randint(0,len(self.solution)-2)
			selected = self.solution[select]
			self.solution[select] = self.solution[select+1]
			self.solution[select+1] = selected
			
initialSetup()
calculateFitness()
print(Population[0].fitness)
for x in range(argGeneration):
	NextGen = newGeneration()
	Population = NextGen
calculateFitness()
print(Population[0].fitness)