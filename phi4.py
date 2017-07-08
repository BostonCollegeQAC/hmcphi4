import lattice as latt
from helper import *

def hmc_update():
    global expdh,phi,acc,rej
    
    oldphi = np.copy(phi)
    pi =  gaussrand(system.v)
    
    s = action(phi,system.hop,system.kappa,system.lamb)
    oldham = (hamiltonian(pi,s))
    
    #molecular dynamics
    for i in range(nhamdyn):
        movephi(phi,pi,eps/2.0)
        movepi(pi,phi,system.hop,system.kappa,system.lamb,eps)
        movephi(phi,pi,eps/2.0)
        
    s = action(phi,system.hop,system.kappa,system.lamb)
    dh = hamiltonian(pi,s) - oldham
 
    expdh += np.exp(-dh)
    
    #metropolis
    if(dh < 0.0):
        acc += 1
    elif(np.exp(-dh) > np.random.uniform(0,1.0)):
        acc += 1
    else:
        rej += 1
        phi = np.copy(oldphi)
    

system = latt.lattice()
tau = 1.0
nhamdyn = 50
niter = 5000
nbin = 500
eps = tau/nhamdyn

acc = 0
rej = 0

phi =  gaussrand(system.v)
expdh = 0.0

m = 0.0
for it in range(niter):
    hmc_update()
    m += abs(magnetization(phi))/system.v
    
    if((it+1)%nbin == 0):
        print("<exp(-del H)> = ",expdh/nbin)
        expdh = 0.0
        
        print("<m> = ",m/nbin)
        m = 0.0
    
        print("acceptance fraction = ",acc/(acc+rej))
