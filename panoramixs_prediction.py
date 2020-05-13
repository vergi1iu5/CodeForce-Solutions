"""
	Algorith:
		get intial value
		check if n and k ara prime
		set limit to itial value * 2
		use sieve of eratos algorith to get next prime num
		check with next input
"""

import math

def main(n, k):
	
	if (n % 2 != 1) or (k % 2 != 1):
		return "Inputs are not prime"

	primes = []
	nums = list(range(2, k + 1))

	while True:
		temp = nums.pop(0)
		primes.append(temp)
		if nums == []: break
		removeMultiples(nums, temp)
	
	primes = primes[-2]

	if primes == n:
		return "YES"
	else:
		return "NO"
	
def removeMultiples(myList, mult):
	# Remove all duplicates of mult from myList
	sentinel = myList[0]

	while True:
		temp = myList.pop(0)
		if temp % mult != 0:
			myList.append(temp)
		if myList[0] == sentinel: break
	return myList

###############################################################
# Solution 2 
###############################################################

def main2(n,k):

	if not (isPrime(n) and isPrime(k)):
		return 'Invalid inputs'

	if k == nextPrime(n):
		return 'YES'
	else:
		return 'NO'

def nextPrime(n):
	while True:
		n += 1
		if isPrime(n): break
	return n

def isPrime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if not (n % i):
			return False
	return True

#################################################################
if __name__ == '__main__':
	n = input("Enter firts prime: ")
	k = input("Enter second prime: ")
	result = main2(int(n), int(k))
	print(result)
