import turtle, time, math, random, sys

if (len(sys.argv)<4):
	print("not enough arguments")
	print("Cities, Population, Mutation")
	sys.exit()

argCities = sys.argv[1]
argPopulation = sys.argv[2]
argMutation = sys.argv[3]

global Cities, Population
Cities = []
#City generation
for x in range(int(argCities)):
	city = [random.randint(0,200), random.randint(0,200)]
	Cities.append(city)
	# print("city "+ str(x+1) + "	[" + str(city[0]) + ", " + str(city[1])+"]")

Population = []
for x in range(int(argPopulation)):
	solution = []
	citysol = Cities[:]
	for x in range(len(Cities)):
		integer = random.randint(0,len(citysol)-1)
		solution.append(citysol[integer])
		citysol.pop(integer)
	# print(solution)
	Population.append(solution)
# print(Population)