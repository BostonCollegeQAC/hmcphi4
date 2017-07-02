import numpy as np

def action(system):
    s = 0.0
    
    for i in range(0,system.v):
        j = 0.0
        for imu in range(0,system.dim):
            j += system.phi[system.hop[i][imu]]

        phi2 = system.phi[i]**2
        s += -2.0*system.kappa*j*system.phi[i] + phi2 + system.lamb*(phi2-1.0)**2

    return s

def magnetization(system):
    m = 0.0
    for i in range(0,system.v):
        m += system.phi[i]

    return m

    
