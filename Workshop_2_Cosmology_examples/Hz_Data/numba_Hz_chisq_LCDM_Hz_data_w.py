from __future__ import print_function
import threading
import numba as nb
import numpy as np
from numpy import genfromtxt
import datetime
from numba import float64,guvectorize
import mpmath as smp

Simpson_N=16


szdat=np.genfromtxt('E:\\NumericalMethod_Statistics_Cosmology_Workshop\Workshop_labs_2\Hz_Data\Hz_2016.csv',delimiter=',',skip_header=0)
z=szdat[:,0]
Hz=szdat[:,1]
sig=szdat[:,2]
Hz_error2 = sig**2


c=299792.45

@nb.jit('float64(float64,float64,float64)')
def Hz_LCDM(zh,Om_l,H0):
        Omega_m=1-Om_l
        Omega_lambda=Om_l 
       
        Omega_r=0.
        
        z=zh
        E=0.0
    
        E=(Omega_lambda + (Omega_m*((1+z)**3)) + (Omega_r*(1+z)**4))**0.5
           
        return float(H0*(E))

Hz_LCDM_v=np.vectorize(Hz_LCDM)
n =30  # Increase this for a finer grid
param=2

ols = np.linspace(0.6, .8, n)



H0s = np.linspace(65.,75.,n)





chi2 = np.ones(n**param) * np.infty # Our chi2 values, set initially to super large values
olv= np.ones(n**param) * np.infty
H0v=np.ones(n**param) * np.infty


@nb.jit('float64[:],float64[:], float64[:],float64[:], float64[:]',parallel=True)
def Chisq_list(ols,H0s,chi2,olv,H0v):
            
            
            
           
            x=0
            for i in range(0,len(ols)):
                
                    for k in range(0,len(H0s)):
                          
                        Hz_model = Hz_LCDM_v(z,ols[i],H0s[k])
                        


                        chi2_test = np.sum( (Hz_model - Hz)**2 / Hz_error2 );
                        chi2[x] = chi2_test
                        olv[x]=ols[i]
                        H0v[x]=H0s[k]

                        
                        x=x+1


a = datetime.datetime.now()
Chisq_list(ols,H0s,chi2,olv,H0v)

b = datetime.datetime.now()



delta = b - a
print(delta)
print(float(delta.total_seconds() * 1000)) # milliseconds
print(a,'a')
print(b,'b')


likelihood = np.exp(-0.5 * (chi2-chi2.min()))
chi_sq_dof=chi2/(len(z)-1.-param)

chisq_file=np.empty((len(chi2),5))
chisq_file[:,0]=chi2
chisq_file[:,1]=likelihood
chisq_file[:,2]=chi_sq_dof
chisq_file[:,3]=olv
chisq_file[:,4]=H0v 
print(chisq_file)
	                
np.savetxt("E:\\NumericalMethod_Statistics_Cosmology_Workshop\Workshop_labs_2\Hz_Data\Hz_chisq_likelihood_reduced-Chisq_omegaLambda_LCDM_H0_parallel_numba.csv",list(chisq_file), delimiter=",") 
	

    