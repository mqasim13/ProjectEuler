# FIND LARGEST PALINDROME FROM 2 3-DIGIT #'s

#STEPS
	# figure out a way to check palindrome (string manip)
		# str(n) == str(n)[::-1] <--- this is how to you check for palindrome
		# 	SECOND WAY OF DOING IT (RETURN 0 FOR TRUE AND -1 FOR FALSE)
		# 	word = "nepalapen"
		#	is_palindrome = word.find(word[::-1])
		#	print is_palindrome
	# figure out a way to multiply numbers from 100-999 (for loops)

#bott has to be the bottom limit -1 (99 makes the bottom limit 100)
def largepalindrome3(top,bott):
	#figure out a way for top and bottom to go down incrementally
	num = 0
	palind = 0
	list_palind = []
	#two for loops to multiply 2 digits 
	for i in range(top, bott, -1):
		for j in range(top, bott, -1):
			num = i*j
			#convert int to str to check palindrome
			num = str(num)
			#palindrome check; if yes add to list
			if num == num[::-1]:
				list_palind.append(int(num))
	#print out highest value in list
	print max(list_palind)

largepalindrome3(999,99)
