#Plotting Fourth Order Runge Kutta Method
import numpy as np
import matplotlib.pyplot as plt
def F(x,y):  #F(x,y)=dy/dx
    return x/y


def RK4(f, a, b, ya, n):
    '''
    f:function
    a:starting point
    b:ending point
    ya:initial value at x=a => y(a)=ya
    n:numbers of samples to determine the size of 'h' or step size or width or delta_x
    '''
    x = np.linspace(a, b, n)
    h = x[1] - x[0]
    ylst = [] #empty list
    yi = ya
    for xi in x:
        ylst.append(yi)  #adding elements to the list of ys
        k1 = h*f(xi, yi) #observe h is with k1 if you are writing h outside then modify k2,k3,k4 accordingly 
        k2 = h*f(xi + 0.5*h, yi + 0.5 * k1)
        k3 = h*f(xi + 0.5*h, yi + 0.5 * k2)
        k4 = h*f(xi + h, yi + k3)
        yi = yi+ (1./6) * (k1 + 2.*k2 + 2.*k3 +k4) #setting new yi for new xi as initial conditions for next step
        y = np.array(ylst)
    return x, y

def fx(x):#analytical solution of dy/dx=x/y , y(0)=1
    return ((x**2)+1)**0.5
yv=np.vectorize(fx)
xin,yrk4=RK4(F,0.,2.,1.,5.)
y=fx(xin)
print(xin,yrk4,y)

plt.plot(xin,y,'r+')
plt.plot(xin,yrk4,'b--')
plt.yscale('log')
plt.show()
