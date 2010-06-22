#Spencer Krum
#June 21
#Collatz Conjecture w/ pickle, pylab and class

import pickle, sys

print "Collatz Conjecture."
print "Collatz conjecture is that any positive integer will become 1 after the following procedure is applied a sufficient number of times."
print "If the number is even, divide it by two. If the number is odd multiply by three and add one."


class Collatz:
	def __init__(self, start, end, lengths):
		self.start = start
		self.end = end
		self.lengths = lengths



def theNumber(prompt):
	while True:	
		number = raw_input(prompt)
		try:	
			number = abs(int(number))
			return number
		except ValueError:
			print "Please enter an integer"


x = 1
lengths = []
#name = raw_input("Name the new file: ")
#start = theNumber("Starting number: ")
#end = theNumber("Ending number: ")
name = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
i = start
while i < end:
#	y, a = collatz_conjecture(i)
	length = 0
	j = i
	while j != 1:
		length += 1
		if j % 2 == 0:
			j /= 2
		else:
			j = j * 3 + 1
	if j % 100 == 0:
		print "The number is %d the number of steps was %d" % (j, length)
	if length > x:
		x = length
		highwater = i
	lengths.append(length)
#	if x <= y:
#		print "The number %d has length %d" % (a, y)
#		x = y
#	highwater.append(y)
#	blank.append(i)
	i += 1
x = Collatz(start, end, lengths)

picklefile = open(name, 'w')
pickle.dump(x, picklefile)


