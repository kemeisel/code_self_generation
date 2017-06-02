from random import randint
from random import choice

buildingBlocks = ["x", "1", "+", "="]
mutations = ["retain", "retain", "retain", "retain", "retain", "retain", "duplicate", "remove", "remove", "addAbove", "addBelow"]
progenitor = [""]
generationNumber = 0
bestResult = 0;


def createNewLine():
	line = ""
	addLine = True
	while addLine:
		line += choice(buildingBlocks) + " "
		addLine = randint(1, 4) >= 2 
	return line


def mutate():
	mutant = []
	for line in progenitor:
		mutation = choice(mutations)
		if (mutation == "retain"):
			mutant.append(line)
		if (mutation == "duplicate"):
			mutant.append(line)
			mutant.append(line)
		if (mutation == "addAbove"):
			mutant.append(createNewLine())
			mutant.append(line)
		if (mutation == "addBelow"):
			mutant.append(line)
			mutant.append(createNewLine())
	return mutant
	

def printNewProgenitor(x, printLines = True):
	print("Best Result: " + str(x))
	print("Generation: " + str(generationNumber))
	if printLines == True:
	    for line in progenitor:
		    print(line)
	    #print()

def main(ancestorResult):
	global bestResult
	global generationNumber
	global progenitor
	for i in range (0, 10000):
		mutant = mutate()
		x = 0
		executable = "\n".join(mutant)
		try:
			exec(executable)
		except:
			continue

		if x > bestResult:
			bestResult = x
			generationNumber += 1
			progenitor = mutant
			printNewProgenitor(x, False)
			main(x)

main(bestResult)
