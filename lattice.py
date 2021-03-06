import numpy as np

class lattice:
    def __init__(self):
        self.dim = 3
        self.l = 6
        self.v = self.l**self.dim

        self.kappa = 0.22
        self.lamb = 1.1689

        self.hop = np.zeros((self.v,2*self.dim),dtype=np.int)

        
        #populate nearest neighbor hopping field
        dmu = -99
        for i in range(0,self.v):
            ll = i
            for mu in range(0,self.dim):
                ltomu = self.l**mu

                imu = (ll//ltomu)%self.l
                
                ll = ll - imu*mu

                if(imu < (self.l-1)):
                    dmu = ltomu
                else:
                    dmu = ltomu*(1-self.l)
                self.hop[i][mu] = i+dmu
                if(imu > 0):
                    dmu = -ltomu 
                else:
                    dmu = -ltomu*(1-self.l)
                self.hop[i][mu+self.dim] = i+dmu
