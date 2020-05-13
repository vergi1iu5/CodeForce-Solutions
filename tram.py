"""
	Algorith:
		add first integer, subtract second 
		create state after each stop
		save max occupancy for each stop
"""

def main(n,stops):
	max_occu = stops[1][0]
	occu = stops[1][0]
	for i in range(1,n):
		occu -= stops[0][i]
		occu += stops[1][i]
		if occu > max_occu:
			max_occu = occu
	return max_occu

if __name__ == '__main__':
	n = int(input('Please enter the number of stops: '))
	stops = [[],[]]
	for i in range(n):
		temp = input('Please enter numbers: ').split(" ")
		a = int(temp[0])
		b = int(temp[1])
		stops[0].append(a)
		stops[1].append(b)
	print(main(n,stops))