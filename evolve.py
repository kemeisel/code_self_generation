from random import randint
from random import choice

buildingBlocks = ["x", "1", "+", "="]
mutations = ["retain", "retain", "retain", "retain", "retain", "retain", "duplicate", "remove", "remove", "addAbove", "addBelow"]
progenitor = [""]
generationNumber = 0
bestResult = 0;

def addToBuildingBlocks(newValue):
    global buildingBlocks
    buildingBlocks.append(newValue)
    print(buildingBlocks)

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

def printNewProgenitor(best, iteration, generation, printLines = True):
    print('Best result: {}, Iteration: {}, Generation: {}'.format(str(best), str(iteration), str(generation)))
    if printLines == True:
        for line in progenitor:
            print(line)

def main(ancestorResult = 0, generation = 1):
    global progenitor
    for iterator in range (0, 10000):
        mutant = mutate()
        x = 0
        executable = "\n".join(mutant)
        try:
            exec(executable)
        except:
            continue
            
        thisResult = x

        # 'executable' acts on thisResult
        if thisResult > ancestorResult:
            progenitor = mutant
            printNewProgenitor(thisResult, iterator, generation)
            addToBuildingBlocks(str(thisResult))
            main(thisResult, generation+1)
            break

main()
