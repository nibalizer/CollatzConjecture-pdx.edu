#Spencer Krum
#Collatz Conjecture
#9 June 2010


print "Collatz Conjecture."
print "Collatz conjecture is that any positive integer will become 1 after the following procedure is applied a sufficient number of times."
print "If the number is even, divide it by two. If the number is odd multiply by three and add one."

def theNumber():
	while True:	
		number = raw_input("Please input a starting integer: ")
		try:	
			number = abs(int(number))
			return number
		except ValueError:
			print "Please enter an integer"
def collatz(number):
	length = 0
	while (number != 1):
		print "The number is %d" % number
		length += 1
		if (number % 2 == 0):
			print "The number is even, therefore divide by two"
			number = number/2
		else:
			print "The number is odd, therefore multiply by three and add one"
			number = (number*3)+1

	print "The number is one, the number of steps was %d" % length
	return length, number
x = 1
for i in range(theNumber()):
	y, a = collatz(i)
	if x <= y:
		print "The number %d has length %d" % (a, y)
		x = y
	
