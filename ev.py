from random import randint
from random import choice
from os import remove

subfolder = 'generations/'

def mutate(parentID, childID):
	lines = []
	for line in open(subfolder + str(parentID) + ".py"):
		if preserve():
			lines.append(line)
		if insert():
			newLine = getNewLine()
			lines.append(newLine);
	saveFile(parentID, childID, lines)
	
			
def saveFile(parentID, childID, lines):
	fileName = str(parentID) + "_" + str(childID) + ".py"
	file = open(subfolder + fileName, "w")
	for line in lines:
		if line != None:
			file.write(line + "\n")
	file.close()
	
	
def insert():
	return randint(1, 10) >= 5
		

def preserve():
	return randint(1, 10) >= 1
		

def getNewLine():
	elements = ["x", "1", "+", "="]
	line = ""
	addLine = True
	while addLine:
		line += choice(elements) + " "
		addLine = randint(1, 4) >= 2 
	return line

	
def cull(parentID, childID):
	global highest
	global best
	fileName = str(parentID) + "_" + str(childID)
	try:
		execfile(subfolder + fileName + ".py")
		#print fileName
		#print y
		if y > highest:
			highest = y
			best = fileName
		else:
			remove(subfolder + fileName + ".py")
	except:
		remove(subfolder + fileName + ".py")	
	

best = "0"
highest = 0;
	
for k in range(1, 101):
	print "Generation " + str(k)
	for j in range(100, 999):	
		mutate(best, j)
		cull(best, j)
	print best		
	print highest
	

	
