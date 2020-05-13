"""
Borze code 
		<<.>> = 0
		<<-.>> = 1
		<<-->> = 2
		algorithm:
			take file as regular
			feed file to processFile funct
			processFile funct == return vecor of nums
			initialize linebuffer
			if len of vecor(i) == 0 , assign to zero
			evaluate if 1 or zero
			output linebuffer
		  
"""

def main(inFileStr):
	lineFeed = processFile(inFileStr)
	lineBuffer = []
	for i in range(len(lineFeed)):
		if len(lineFeed[i][0]) == 1:
			lineBuffer.append('0')
		elif lineFeed[i][0] == "-.":
			lineBuffer.append('1')
		else:	
			lineBuffer.append('2')
	return "".join(lineBuffer)

def processFile(inFileStr):
	inFile = open(inFileStr, 'r')
	code = inFile.readline().strip()
	outBuffer = []
	next_item = 0
	for i in range(len(code)):
		if code[i] == '.' and i == next_item:
			next_item = i + 1
			outBuffer.append([code[i]])
		elif i == next_item:
			next_item = i + 2
			outBuffer.append([code[i:next_item]])
	return outBuffer

if __name__ == '__main__':
	fileStr = input("Enter file name: ")
	print(main(fileStr))