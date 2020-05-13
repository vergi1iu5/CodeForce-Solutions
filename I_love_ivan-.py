def main(n, scores):
	minimum = scores[0]
	maximum = scores[0]
	count = 0
	for i in range(1, len(scores)):
		if scores[i] > maximum:
			maximum = scores[i]
			count += 1
		if scores[i] < minimum:
			minimum = scores[i]
			count += 1

	return count

if __name__ == '__main__':
	n = int( input('Enter number of scores: '))
	scores = input('Enter all scores: ').split(" ")
	scores = [int(score) for score in scores]
	print( main(n, scores))