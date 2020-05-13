"""
	algorith:
		get input number
		convert to integer
		count number of digits, determine if 4 or 7
		if not, print no
		if yes, go thorugh every digit and break if 4 or 7 not met
"""

def main(digit):
	count = 0
	while digit != 0:
		if (digit % 10 == 4 or digit % 10 == 7):
			count += 1
		digit = digit // 10

	if (count == 4 or count == 7):
		return 'YES'
	else:
		return 'NO'

if __name__ == '__main__':
	input_num = input("Enter number: ")
	print(main(int(input_num)))