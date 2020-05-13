def main(k,l,n,p,d):
	
	# if any integer is 1, just return total number of dragons
	if k == 1 or l == 1 or n == 1 or p == 1:
		return d

	input_seq = [k,l,n,p]
	keep = [] #used to store all integers without any multiples
	
	while True:
		temp = input_seq.pop(0)
		keep.append(temp)
		if input_seq == []: break
		removeMultiples(input_seq, temp)
	pre_sum = getModers(keep, d)
	out = 0
	for value in pre_sum: out += value
	return out


def removeMultiples(myList, mult):
	# Remove all duplicates of mult from myList
	sentinel = myList[0]
	while True:
		temp = myList.pop(0)
		if temp % mult != 0:
			myList.append(temp)
		if myList[0] == sentinel: break
	return myList

def getModers(inList, d):
	out = [0]
	for i in range(len(inList)):
		if i == 0:
			out.append(d // inList[i])
		else:
			temp = d // inList[i]
			rem = temp
			for j in range(i):
				rem -= temp // inList[j]
			out.append(rem)
	return out

if __name__ == '__main__':
	k = int(input('Enter first number: '))
	l = int(input('Enter second number: '))
	n = int(input('Enter third number: '))
	p = int(input('Enter last number: '))
	d = int(input('Enter total number: '))
	print(main(k,l,n,p,d))