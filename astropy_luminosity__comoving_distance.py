#Task 2 Comoving and luminosity distances using astropy.cosmology
#Read more http://docs.astropy.org/en/stable/cosmology/
#http://docs.astropy.org/en/stable/index.html

from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
print(cosmo)

#redshift
z=4.0
#luminosity distance
luminositydistance=cosmo.luminosity_distance(z)

#comoving distance using luminosity distance in flat lambda cdm
comovingdistance=luminositydistance/(1.+z)

print('comoving distance in Mpc')   
print(comovingdistance)

print('luminosity distance in Mpc')   
print(luminositydistance)

