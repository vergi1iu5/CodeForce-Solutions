"""
	get n
	get string
	start at begining of string
	if next color is not same, deduct one from n
"""

def main():
	n, stones = getInput()
	stones = [char for char in stones]
	char = stones[0]
	out = 0
	for nextChar in stones[1:n]:
		if nextChar == char:
			out += 1	
		char = nextChar
	return out

def getInput():
	n = input('Enter number of stones: ')
	n = int(n)
	stones = input('Enter arrangement of stones: ')
	return n, stones

if __name__ == '__main__':
	print(main())