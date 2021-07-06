#Fourth Order Runge Kutta Method

def Fn(y,x):  #F(x,y)=dy/dx
    return x/(y**2)
    
t0=0
y0=2
h=0.5   #to calculate value of y1=y(t) at t=t0+h using y0=y(t0)

def RK4(F,y0,t0,h):
    K1=F(y0,t0)
    K2=F(y0+K1*(h/2.),t0+(h/2.))
    K3=F(y0+K2*(h/2.),t0+(h/2.))
    K4=F(y0+K3*h,t0+h)

    y1=y0+(K1+2*K2+2*K3+K4)*(h/6.)
    return y1
    

print(RK4(Fn,y0,t0,h))
