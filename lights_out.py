"""
	Algorith:
		get all 3 rows and place in a list of 3 lists
		add all adjectent places in the matrix
		if place is odd, set to zero, else set to 1
"""

from copy import deepcopy

def main(inFileStr):
	matrix = processFile(inFileStr)
	addedMatrix = deepcopy(matrix)
	finalMatrix = [[1,1,1],[1,1,1],[1,1,1]]
	for i in range(3):
		for j in range(3):
			if j - 1 >= 0:
				try:
					addedMatrix[i][j] += matrix[i][j - 1]
				except:
					pass
			
			try:
				addedMatrix[i][j] += matrix[i][j + 1]
			except:
				pass
			
			if i - 1 >= 0:		
				try:
					addedMatrix[i][j] += matrix[i - 1][j]
				except:
					pass
						
			try:
				addedMatrix[i][j] += matrix[i + 1][j]
			except:
				pass
					
			if ((addedMatrix[i][j] % 2) == 1):
				finalMatrix[i][j] = 0
	return finalMatrix

def processFile(inFileStr):
	inFile = open(inFileStr, 'r')
	matrix = []
	for i in range(3):
		row = inFile.readline().strip().split(" ")
		matrix.append([int(i) for i in row])
	return matrix

if __name__ == '__main__':
	fileStr = input("Enter file name: ")
	print(main(fileStr))			