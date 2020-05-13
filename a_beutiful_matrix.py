"""
	imput: a i = 5 by j = 5 matrix
	matrix has 24 0 and a single 1

	goal: Calculate minimum number of colum or row
	swaps needed to move 1 to center

	steps:
		place matrix in a single row (stack each column)
		get index of 1
		get modulus and remainder of index with 5
		get abs(modulus - 2) == num of column swaps
		get abs(rem - 3) == num of row swaps
		add num of row and colum swaps
"""

def main(inFileStr):
	inFile = open(inFileStr, 'r')
	matrix_to_row = linearizeMatrix(inFile)
	one_index = getIndex(matrix_to_row)
	mod = one_index // 5
	rem = one_index % 5
	num_colum_sw = abs(mod - 2)
	num_row_sw = abs(rem - 3)
	close(inFile)
	return num_colum_sw + num_row_sw

def linearizeMatrix(inFileObj):
	matrix_buff = []
	for line in inFileObj.readlines():
		row = line.strip().split(" ")
		matrix_buff.extend(row)
	return matrix_buff

def getIndex(inVector):
	for i in range(len(inVector)):
		if inVector[i] == '1':
			break
	return i + 1

if __name__ == '__main__':
	fileStr = input("Enter file name: ")
	print(main(fileStr))