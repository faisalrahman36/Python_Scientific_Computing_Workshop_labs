import numpy as np
Simpson_N=100  

def fn(x):
    return x**6 + 2*x

def intfn(x):
    return ((x**7)/7.) + x**2.
    
def fs(x):
    return np.sin(x) + x**7
#Composite Simpson's Rule
def ssin(f,a,b):
    fv = np.vectorize(f)
    
    result=0.
    N=Simpson_N  #Simpson's Rule order
    i=np.arange(0,N)*1.
    j=np.arange(1,N)*1.
    
    h=(b-a)/N
    result=(h/6.)*(fv(a)+ 4*np.sum(fv(a + (i+0.5)*h)) + 2*np.sum(fv(a + j*h)) + fv(b) )
    return result

#Basic Simpson's Rule
def int_simpsons(f,a,b):
    I=0.
    h=(b-a)/6.
    m=(a+b)/2.
    I=(f(a)+4*f(m)+f(b))*h
    return I

#print(ssin(np.sin,1,2))
print(ssin(fn,0,3))
print(int_simpsons(fn,0,3))
print(intfn(3.)-intfn(0.))    
#print(ssin(fs,1,5.),'definite integral of f(x)=sin(x) + x^7 with a=1 and b=5 using N/2 =', Simpson_N )
#print(int_simpsons(fs,1,5.),"definite integral of f(x)=sin(x) + x^7 with a=1 and b=5 using Basic Simpson's Rule")

