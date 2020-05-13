"""
	Algorith:
		find max and index of max  imin
		find min and index of max imax
		allow for index change if values are same
		return imax + (n - imin)
"""

def main(n, line):
	
	maxHeight = line[0]
	imax = 0
	minHeight = line[-1]
	imin = n

	for i in range(n):
		if line[i] > maxHeight:
			maxHeight = line[i]
			imax = i
			next

		if line[i] <= minHeight:
			minHeight = line[i]
			imin = i

	if imin < imax:
		bias = 2
	else:
		bias = 1
		
	return imax + (n - imin - bias)

if __name__ == '__main__':
	n = input("Enter numer of solders: ")
	line = input("Enter heights separated by space: ")
	line = line.split(" ")
	line = [int(value) for value in line]
	print(main(int(n), line))


