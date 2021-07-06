#Task 1 Calculate Comoving and Luminosity distance using Simpson's Rule in Flat-Lambda CDM universe
Omega_m=.3 
Omega_lambda=0.7
H0=70.
c=299792.458
def Ez(z):
    z=z
    E=0.0
    E=(Omega_lambda + (Omega_m*((1+z)**3)))**0.5 #for flat LCDM
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
    

print('comoving distance in Mpc')   
print(comoving_distance(4.))

print('luminosity distance in Mpc')   
print(luminosity_distance(4.))