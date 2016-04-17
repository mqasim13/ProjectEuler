#SUMMING MULTIPLES OF 3 AND 5 (UNDER 1000)

# defines the top limit of range
def multiple35(limit):
	sum = 0
	for i in range(1, limit):
		# Check to see if divisible by 5, if so add to sum
		if i % 5 == 0:
			sum += i
		# Check to see if divisible by 3, if so add to sum
		elif i % 3 == 0:
				sum += i
		# If neithe of the above keep sum the same
		else:
			sum = sum
	return sum


x = multiple35(1000)
print x