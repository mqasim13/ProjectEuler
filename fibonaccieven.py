# SUM THE EVEN FIBONACCI NUMBERS UNDER 4 MILLION

def fibonaccieven():
	a, b = 1, 1
	total = 0
	# ensures that the number of fibonnaci numbers is under 4 million
	while a <= 4000000: 
	    if a % 2 == 0:
	        total += a
	     # the real formula for Fibonacci sequence
	    a, b = b, a+b 
	print total

fibonaccieven()