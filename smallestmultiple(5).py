# FIND THE SMALLEST NUMBER THAT IS A MULTIPLE OF ALL #'s BETWEEN 1-20
# answer is 2^4 * 3^2 * 5 * 7 * 11 * 13 * 15 * 17 * 19 = 232792560


# ****NEED TO COMPLETE THIS CODE*** 
def smallestmutiple(bottom, top):
	prime = []
	#iterate through range and adds prime numbers to list
	for num in range(bottom, top):
		if num > 1:
			for i in range(2, num):
				if (num % i) == 0:
					break
			else:
				prime.append(num)
	#figure out how to get 2^4 and 3^2
	#some sort of looping mechanism 
	
		




		

smallestmutiple(1, 20)

