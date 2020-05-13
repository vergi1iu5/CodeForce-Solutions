"""
	input: unique year
	output: next year where all digits are unique

	Algorith:
		Add one to year
		check if all digits uniquq
		repeat if not, return if unique
"""

def main(inFileStr):
	year = processFile(inFileStr)
	nextYear = getNextYear(year)
	return nextYear

def getNextYear(initYear):
	year = int(initYear)
	year += 1
	if uniqueYear(str(year)):
		return year
	else:
		return getNextYear(year)

def uniqueYear(year):
	vectYear = [char for char in year]
	vectYear.sort()
	unique = True
	for i in range(len(vectYear) - 1):
		if vectYear[i] == vectYear[i + 1]:
			unique = False
	return unique

def processFile(inFileStr):
	inFile = open(inFileStr)
	year = inFile.readline().strip()
	return year

if __name__ == '__main__':
	fileStr = input("Enter file name: ")
	print(main(fileStr))