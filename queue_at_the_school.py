"""
Algorithm:
	get input of num of kids n
	get input for num of iterations t
	get string, sptrip of carriage return and split into char
	iterate t
		iterate 0  to n - 2
			if i == "B" and i + 1 == "G", trade palces
	concatanate string
	output string
"""

def main(inFileStr):
	n, t, line = processFile(inFileStr)
	for tt in range(t):
		allow_chg = 0
		for nn in range(n - 1):
			if line[nn] == 'B' and line[nn + 1] == 'G' and allow_chg == nn:
				line[nn] = 'G'
				line[nn + 1] = 'B'
				allow_chg += 2
			elif nn == allow_chg:
				allow_chg += 1
	return "".join(line)

def processFile(inFileStr):
	inFile = open(inFileStr, 'r')
	temp = inFile.readline().strip().split(" ")
	queue = inFile.readline().strip()
	return int(temp[0]), int(temp[1]), [char for char in queue]

if __name__ == '__main__':
	fileStr = input("Enter file name: ")
	print(main(fileStr))
