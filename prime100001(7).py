#WHAT IS THE 10,001st PRIME NUMBER

#find all prime numbers 

#def prime100001():
	#create a list of prime numbers [while loop to stop at specific length]
	#find the 10,0001st item in list
	#ALTERNATIVE: Create a counter to track the changes of prime
	#return the 10,0001 prime
def prime10001():
	lower = int(input("Enter lower range: "))
	upper = int(input("Enter upper range: "))

	prime = []
	for num in range(lower,upper + 1):
	   # prime numbers are greater than 1
	   if num > 1:
	       for i in range(2,num):
	           if (num % i) == 0:
	               break
	       else:
	           prime.append(num)
	           listlen = len(prime)
	           print listlen
	           if listlen == 10001:
	           	return prime[listlen - 1]
 
print prime10001()

#answer is 104743
#TODO
# Make this more efficient 
# Use the counter method 