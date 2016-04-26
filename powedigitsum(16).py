#FIND THE SUM OF ALL THE DIGITS IN 2^1000

def powerdigitsum():
	num = str(2**1000)
	total = 0
	for i in num:
		i = int(i)
		total += i
	return total

print powerdigitsum()