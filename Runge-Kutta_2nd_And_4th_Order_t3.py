#Lab 5: Task 3:  Comparing Second Order Runge-Kutta (Heun's method) and Fourth Order Runge-Kutta Methods
import numpy as np
import matplotlib.pyplot as plt
def F(x,y):  #F(x,y)=dy/dx
    return 6*(y**2)*x
def RK2(f, a, b, ya, n):
    '''
    f:function
    a:starting point
    b:ending point
    ya:initial value at x=a => y(a)=ya
    n:numbers of samples to determine the size of 'h' or step size or width or delta_x
    '''
    x = np.linspace(a, b, n)
    h = x[1] - x[0]
    ylst = []
    yi = ya
    for xi in x:
        ylst.append(yi)
        k1 = f(xi, yi)
        k2 = f(xi + h, yi + h * k1)
        yi = yi+ 0.5 * h * (k1 + k2)
        y = np.array(ylst)
    return x, y


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

def fx(x):#analytical solution of dy/dx=6*(y**2)*x , y(1)=1/25
    return 1./(28.-3*(x**2))
yv=np.vectorize(fx)
xin2,yrk2=RK2(F,1.,3.,1./25.,10.)
xin,yrk4=RK4(F,1.,3.,1./25.,10.)

y=fx(xin2)

plt.plot(xin,y,'r-')
plt.plot(xin,yrk4,'g+')

plt.plot(xin2,yrk2,'bs')
#plt.yscale('log')
plt.show()

'''
HW Task 1: Manually solve dy/dx= 6xy^2 with y(1)=1/25 for Y(x) with x=1.1, 1.2, 1.3, 1.4, 1.5 using both Runge-Kutta Second and Fourth Order Methods

HW Task 2: Compare with the analytical solution and see which method gives better results.

HW Task 3: Repeat Tasks 1 and 2 for dy/dx= (3x^2+4x -4)/(2y-4) for  y(1)=3 with x= 1.1, 1.2, 1.3, 1.4, 1.5


'''