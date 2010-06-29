from matplotlib import *
from pylab import *
from collatz import CollatzGenerator

ion()

plot(range(2, 801), list(CollatzGenerator(800)), ".")
ylabel('number at step')
xlabel('step number')
grid(True)

raw_input("lasers")