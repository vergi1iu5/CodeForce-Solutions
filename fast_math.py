def main(a, b):
	result = []
	for i in range(len(a)):
		temp = ((not a[i]) and b[i]) or (a[i] and (not b[i]))
		if temp:
			temp = 1
		else:
			temp = 0
		result.append(temp)
	return "".join([str(value) for value in result])

if __name__ == '__main__':
	a = input('Enter first number: ')
	b = input('Enter second number: ')
	a = [int(value) for value in a]
	b = [int(value) for value in b]
	print(main(a,b))

"""
	Algorith:
		get interger
		check if it's 1 or 0
		create array with n elements
		set n element to rand num up to n
		if rand num is i, try again
		return n elemts
"""