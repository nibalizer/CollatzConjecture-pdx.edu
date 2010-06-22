#Spencer Krum
#June 21
#Collatz Conjecture w/ pickle, pylab and class

import pickle, sys, time


print "Collatz Conjecture."
print "Collatz conjecture is that any positive integer will become 1 after the following procedure is applied a sufficient number of times."
print "If the number is even, divide it by two. If the number is odd multiply by three and add one."
print time.ctime()
starttime = time.time()

class Collatz:
	def __init__(self, start, end, lengths, highwater, lengthhighwater):
		self.start = start
		self.end = end
		self.lengths = lengths
		self.highwater = highwater
		self.lengthhighwater = lengthhighwater



def theNumber(prompt):
	while True:	
		number = raw_input(prompt)
		try:	
			number = abs(int(number))
			return number
		except ValueError:
			print "Please enter an integer"


x = 1
lengths = [1]
#name = raw_input("Name the new file: ")
#start = theNumber("Starting number: ")
#end = theNumber("Ending number: ")
name = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
steps = int(sys.argv[4])
i = start
while i < end:
#	y, a = collatz_conjecture(i)
	length = 0
	j = i
	while j != 1:
		if j < i:
			length = lengths[j] + length
			j = 1
		else:	
			length += 1
			if j % 2 == 0:
				j /= 2
			else:
				j = j * 3 + 1
	if i % steps == 0:
		print "The number is %d the number of steps was %d" % (i, length)
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
x = Collatz(start, end, lengths, highwater, x)

title_ = "The longest run was %d, the number was %d" % (x.lengthhighwater, x.highwater)
print title_
#picklefile = open(name, 'w')
#pickle.dump(x, picklefile)
print time.ctime()
endtime = time.time()
totaltime = endtime - starttime
print "Total elapsed time is %d seconds" % totaltime


