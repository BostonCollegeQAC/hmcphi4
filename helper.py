import numpy as np

def action(phi,hop,kappa,lamb):
    s = 0.0
    size = len(phi)
    dim = len(hop[0])//2
    
    for i in range(0,size):
        phi_nnsum = 0.0
        #sum over positive direction only
        for imu in range(0,dim):
            phi_nnsum += phi[hop[i][imu]]

        phi2 = phi[i]**2
        s += -2.0*kappa*phi_nnsum*phi[i] + phi2 + lamb*(phi2-1.0)**2

    return s

def hamiltonian(pi,s):
    h = 0.0
    size = len(pi)

    for i in range(0,size):
        h += pi[i]**2

    return 0.5*h + s
    

def magnetization(field):
    return np.sum(field)

def gaussrand(size):
    #std. dev = 1.0, mean = 0.0
    return np.random.normal(0,1.0,size)

##leap-frog methods:
def movepi(pi,phi,hop,kappa,lamb,eps):
    size = len(phi)
    twodim = len(hop[0])

    for i in range(0,size):
        phi_nnsum = 0.0
        for imu in range(0,twodim):
            phi_nnsum += phi[hop[i][imu]]

        pi[i] += eps*(2.0*kappa*phi_nnsum - 2.0*phi[i] \
                    - 4.0*lamb*(phi[i]**2-1.0)*phi[i])

def movephi(phi,pi,eps):
    size = len(pi)

    for i in range(0,size):
        phi[i] += eps*pi[i]
##
