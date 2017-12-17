import turtle, time, math, random, sys, copy

if (len(sys.argv)<6):
	print("not enough arguments")
	print("Cities, Population, Selection, Mutation, Generation")
	sys.exit()

global Cities, Population, Generation, Selection, argGeneration
	
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
		city = [random.randint(0,200), random.randint(0,200)]
		Cities.append(city)
		print("city "+ str(x+1) + "	[" + str(city[0]) + ", " + str(city[1])+"]")

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
	for x in range(len(Population)):
		print(Population[x].fitness)

		
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
		print(k)
		Selected.append(copy.deepcopy(Population[k-1]))
	
	
def newGeneration():
	calculateFitness()
	select()
		
		
class Solution():
	def __init__(self, solution):
		self.solution = solution
		self.fitness = 0
	
	def calcfitness(self):
		self.fitness = 0
		for x in range(len(self.solution)-1):
			self.fitness += math.sqrt(math.pow(self.solution[x+1][0]-self.solution[x][0],2)+math.pow(self.solution[x+1][1]-self.solution[x][1],2));

initialSetup()
newGeneration()