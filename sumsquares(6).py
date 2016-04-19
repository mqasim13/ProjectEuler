#FIND THE DIFFERENCE BETWEEN THE SUM OF SQUARES (1-100)
#AND THE SQUARE OF THE SUM 


def sumsquares(toplimit):
	sumtosquare = 0
	sumsquared = 0
	sumofsquares = 0
	differnce = 0
	#sum all numbers between 1 and toplimit
	for i in range(toplimit + 1):
		sumtosquare += i
		#print sumtosquare
	#sum all squares of number between 1 and toplimit
	for i in range(toplimit + 1):
		sumofsquares += i ** 2
		#print sumofsquares
	#square the sum of numbers between 1 and toplimit
	sumsquared = sumtosquare ** 2
	#print sumsquared
	difference = sumsquared - sumofsquares
	print difference

sumsquares(100)