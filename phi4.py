import lattice as latt
from helper import *

system = latt.lattice()
tau = 1.0
nstep = 100
eps = tau/nstep

phi =  gaussrand(system.v)
pi =  gaussrand(system.v)

s = action(phi,system.hop,system.kappa,system.lamb)
print(hamiltonian(pi,s))

#m1 = magnetization(phi)
#print(m1*m1/system.v)

#molecular dynamics
for i in range(nstep):
    movephi(phi,pi,eps/2.0)
    movepi(pi,phi,system.hop,system.kappa,system.lamb,eps)
    movephi(phi,pi,eps/2.0)
    
    s = action(phi,system.hop,system.kappa,system.lamb)
    print(hamiltonian(pi,s))


