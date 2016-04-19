# FIND THE SMALLEST NUMBER THAT IS A MULTIPLE OF ALL #'s BETWEEN 1-20
# answer is 2327992560 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19
def smallestmutiple(bottom, top):
	for num in range(bottom, top):
		if num > 1:
			for i in range(2, num):
				if (num % i) == 0:
					break
			else:
				print(num)

smallestmutiple(2, 10)