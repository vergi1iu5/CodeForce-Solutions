"""
	Algorith:
		randomly create all n numbers
		run through every and check that i is not in the ith place
		reduce n by one if we need to change to different number
		add to list in order if kept
		check with list to assure uniqueness
"""

class toggler():
	
	def __init__(self):
		self.value = 1

	def toggle(self):
		if self.value == 1:
			self.value = -1
		else:
			self.value = 1		

def main(n):
	if n == 1:
		return -1
	
	bias = toggler()

	output = []
	for i in range(1, n + 1):
		output.append( i + bias.value)
		bias.toggle()

	if n%2 == 1:
		output[-1], output[-2] = output[-2], output[-1] - 1

	return output

if __name__ == '__main__':
	
	n = input('enter permuatation length: ')

	print(main(int(n)))