#LARGEST PRIME FACTOR OF 600851475143

def largeprimefactor(num):
	i = 2
	while i * i <= num:
		if num % i:
			i += 1
		else:
			num //= i # // means floor division
	return num

print largeprimefactor(600851475143)
