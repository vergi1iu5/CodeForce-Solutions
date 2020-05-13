"""
	Algorithm:
		create list of characters
		init upper and lower
		get value of char and associate to respective letter, increase respective counter
		assign bias depending if we need to upper case or lower case
		add bias to every character

"""

def main(inFileStr):
	
	word = getWord(inFileStr)
	wordValue = [ord(char) for char in word]
	upperCase = [[0],[]]
	lowerCase = [[0],[]]
	
	for i in range(len(wordValue)):
		if wordValue[i] >= 97:
			upperCase[0][0] += 1
			upperCase[1].append(i)
		else:
			lowerCase[0][0] += 1
			lowerCase[1].append(i)
	decision = upperCase[0][0] - lowerCase[0][0]
	
	if decision < 0:
		bias = -32
		indexes = upperCase[1].copy()
	else:
		bias = 32
		indexes = lowerCase[1].copy()

	for i in indexes:
		wordValue[i] += bias

	finalWord = [chr(value) for value in wordValue]

	return "".join(finalWord)

def getWord(inFileStr):
	inFile = open(inFileStr, 'r')
	word = inFile.readline().strip()
	return word

if __name__ == '__main__':
	fileStr = input("Enter file name: ")
	print(main(fileStr))
