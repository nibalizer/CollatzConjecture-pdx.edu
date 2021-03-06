#Spencer Krum
#Collatz Conjecture with live graphing
#10 June 2010

from pylab import *
from matplotlib import *

import pickle

print "Collatz Conjecture."
print "Collatz conjecture is that any positive integer will become 1 after the following procedure is applied a sufficient number of times."
print "If the number is even, divide it by two. If the number is odd multiply by three and add one."


class Collatz:
	def __init__(self, start, end, highwater,blank):
		self.start = start
		self.end = end
		self.highwater = highwater
		self.blank = blank



def theNumber(prompt):
	while True:	
		number = raw_input(prompt)
		try:	
			number = abs(int(number))
			return number
		except ValueError:
			print "Please enter an integer"
def collatz_conjecture(number_):
	length = 0
	number = number_
	while (number != 1):
	#	print "The number is %d" % number
		length += 1
		if (number % 2 == 0):
	#		print "The number is even, therefore divide by two"
			number = number/2
		else:
	#		print "The number is odd, therefore multiply by three and add one"
			number = (number*3)+1

	if number_ % 100 == 0:
		print "The number is %d the number of steps was %d" % (number_, length)
	return length, number
ion()
x = 1
highwater = []
blank = []
name = raw_input("Name the new pickle file: ")
start = theNumber("Starting number: ")
end = theNumber("Ending number: ")
i = start
name = raw_input("Please give the name of the file you would like to save the resulting graph in: ")
plot(blank, highwater, 'o')
ylabel('Number of steps to one')
xlabel('Initial number')
grid(True)

while i < end:
	y, a = collatz_conjecture(i)
	if x <= y:
		print "The number %d has length %d" % (a, y)
		x = y
	highwater.append(y)
	blank.append(i)
	plot(blank[i-1], highwater[i-1], 'bd')
	pylab.axis([0,i,None,None])
	blank.append(i)
	ylabel('Number of steps to one')
	xlabel('Initial number')
	grid(True)
	draw()
	hold(True)
	i += 1

#x = Collatz(start, end, highwater, blank)

#picklefile = open(name, 'w')
#pickle.dump(x, picklefile)

plot(blank, highwater, 'o')
ylabel('Number of steps to one')
xlabel('Initial number')
grid(True)
draw()
hold(False)
savefig(name)
raw_input("Press return to quit")
