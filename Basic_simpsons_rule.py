import mpmath as smp
from math import sin

def fx(x):
    return x**2

def fsin(x):
    return sin(x)

def int_simpsons(f,a,b):
    I=0.
    h=(b-a)/2.
    I=(f(a)+4*(f((a+b)/2.))+f(b))*(h/3.)
    return I
    
print(int_simpsons(fx,1.,3.))
print(int_simpsons(fsin,1.,3.))
