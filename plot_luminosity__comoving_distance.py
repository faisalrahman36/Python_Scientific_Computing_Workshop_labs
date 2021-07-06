#Task 3 Plotting comoving and luminosity distances calculated using simpsons rule
import numpy as np
import matplotlib.pyplot as plt
Omega_m=.3 
Omega_lambda=0.7
H0=70.
c=299792.458
def Ez(z):
    z=z
    E=0.0
    E=(Omega_lambda + (Omega_m*((1+z)**3)))**0.5
    return E

def one_div_H_Ez(zh):
    return 1.0/(H0*Ez(zh))
    
def int_simpsons(f,a,b):
    I=0.
    h=(b-a)/2.
    I=(f(a)+4*(f((a+b)/2.))+f(b))*(h/3.)
    return I

#Comoving distance
def comoving_distance(z):
    
    comovingdistance = int_simpsons(one_div_H_Ez,0.,z)*c
    return comovingdistance
    
def luminosity_distance(z):
    luminositydistance=(1+z)*comoving_distance(z) #for flat lambda cdm
    return luminositydistance
    
z=np.linspace(0.,5.,num=10)

plt.plot(z,comoving_distance(z),'b+')
plt.plot(z,luminosity_distance(z),'r--')
plt.xlabel('redshift z')
plt.ylabel('comoving/luminosity distances in Mpc')
plt.title('comoving/luminosity distances for different redshift values')

plt.show()

#HW Task 1: Plot the same using astropy
#HW Task 2: Plot comoving and luminosity distances using H0 and Omega_m from Planck 2015 parameters