"""
	Algorithm for next problem:
		take the n number and get all lines at ones. 
		Add all the left integers
		Add all the right integers
		subtract from 5 each sum store seperateky
		if result is greater than half, then most were closed, keep result
		if result is less than half, then most were open, take n - result
		retunr left result + right result
"""

def main(n,left,right):
	l = 0
	for value in left:
		l += value
	r = 0
	for value in right:
		r += value

	threshold = n / 2

	rl = n - l
	rr = n - r

	if rl > threshold:
		out = l
	else:
		out = rl

	if rr > threshold:
		out += r
	else:
		out += rr

	return out

if __name__ == '__main__':
	n = int(input('Enter number of cupboards: '))
	left = []
	right = []
	for i in range(n):
		line = input('Enter cupboard: ').split(" ")
		l, r = int(line[0]), int(line[1])
		left.append(l)
		right.append(r)
	print(main(n, left, right)) 
