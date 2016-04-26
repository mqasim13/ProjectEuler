#FIND THE PYTHAGOREAN TRIPLET FOR WHICH a+b+c = 1000


def pythagtriplet():
	#400 is arbitrary number (350 didn't work)
	for a in range(400):
		for b in range(a+1, 400):
			c = 1000 - (a+b)
			if a*a + b*b == c*c:
				# so that I know what the actual triplet actually is
				print (a,b,c)
				return a*b*c

print pythagtriplet()
