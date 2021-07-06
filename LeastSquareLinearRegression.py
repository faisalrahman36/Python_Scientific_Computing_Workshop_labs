#Task 2: Implement  least-squares linear regression
import numpy as np
y=[2.1,4.1,6.1,8.1,10.1,12.1,14.1,16.1,18.1,20.1]
x=[1,2,3,4,5,6,7,8,9,10]


xy=[m*n for m,n in zip(x,y)]
sumx=np.sum(x)
sumy=np.sum(y)
n=len(x)  #or y as both should be same to make it work
a=np.sum(xy)
b=(1./n)*sum(x)*sum(y)
c=sum([e*f for e,f in zip(x,x)])
d=(1./n)*(sum(x)**2)

meanx=np.mean(x)
meany=np.mean(y)


b1=(a-b)/(c-d)
print(b1)

b0=meany-b1*meanx
print(b0)
#Line y_est=beta1*x + beta0

def y_est(x,beta1,beta0):
    yest=beta1*x+beta0
    return yest
    
print(y_est(11,b1,b0))

#HW Task 2: a)Implement code to find correlation coefficient 'r'
#           b) Use correlation coefficient r to calculate beta1=r*(sy/sx)
#           c) Check if new beta1 is same as the beta1=b1 calculated in our lab task 2 code.