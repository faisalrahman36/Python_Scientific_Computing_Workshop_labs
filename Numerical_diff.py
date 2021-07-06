#Numerical differentiation
import numpy as np
import matplotlib.pyplot as plt
def fun(x):
    return 4*(x**3) + 2*(x**2)
    
def der_true(x):
    return 12*(x**2) + 4*x
    
def bwd(f,x,h):
    m=x-h
    df=(f(x)-f(m))/h
    return df
    
def fwd(f,x,h):
    l=x+h
    df=(f(l)-f(x))/h
    return df
    
def cd(f,x,h):
    m=x-h
    l=x+h
    df=(f(l)-f(m))/(2*h)
    return df
    
samples=30
h=0.1
xs=np.linspace(1,20,num=samples)
yb=np.linspace(1,20,num=samples)
yf=np.linspace(1,20,num=samples)
yc=np.linspace(1,20,num=samples)
true=np.linspace(1,20,num=samples)

for i in range(0,len(xs)):
    yb[i]=bwd(fun,xs[i],h)
    yf[i]=fwd(fun,xs[i],h)
    yc[i]=cd(fun,xs[i],h)
    true[i]=der_true(xs[i])

plt.plot(xs,yb,'r.')
plt.plot(xs,yf,'b.')
plt.plot(xs,yc,'g.')
plt.plot(xs,true,'k-')

    
plt.show()

