

from matplotlib import *
from pylab import *


def collatz(number_):
	length = [0]
	number = [number_]
	while (number[-1] != 1):
		length.append(length[-1] + 1)
		if ((number[-1] % 2) == 0):
			number.append(number[-1]/2)
		else:
			number.append((number[-1]*3)+1)

	return length, number
#5036807898

x = raw_input("please enter your number: ")
y, z = collatz(float(x))

print y, z



ion()
plot(y, z, '-')
ylabel('number at step')
xlabel('step number')
grid(True)


raw_input("lasers")
