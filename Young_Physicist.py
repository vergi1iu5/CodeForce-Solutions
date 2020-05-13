################################################
#algorith:
#
#open input file
#read first line and asses:
#	if interger <= 0
#		print yes, end program
#
#for i in range(first line - 1)
#		read next line 
#		divide into xi, yi, and zi (function)
#		if i is 0
#			if x + xi or y + yi or z + zi is not 0
#				break
#		else
#			add xi, yi, and zi to each
#else
#	return no
##################################################


def main(inFileStr):
	inFile = open(inFileStr, "r")
	numVec = inFile.readline()
	if numVec == 0:
		return "YES"
	else:
		return addVectors(int(numVec), inFile)

def addVectors(numVec, inFileObj):
	x, y, z = 0, 0, 0
	for i in range(numVec - 1, -1, -1):
		xi, yi, zi = divideInputs(inFileObj)
		if i == 0:
			if ((x + xi != 0) or (y + yi != 0) or (z + zi != 0)):
				return "NO"
		else:
			x = x + xi
			y = y + yi
			z = z + zi
	else:
		return "YES"

def divideInputs(inFileObj):
	nextVect = inFileObj.readline().split(" ")
	return int(nextVect[0]), int(nextVect[1]), int(nextVect[2])

if __name__ == '__main__':
	fileStr = input("Enter file name: ")
	print(main(fileStr))
