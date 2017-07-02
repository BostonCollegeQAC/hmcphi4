import lattice as latt
from helper import *

system = latt.lattice()

#print(system.phi)

s = action(system)
print(s)

m = magnetization(system)
print(m*m/system.v)
