# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:16:38 2021

@author: JOSE
"""

import numpy as np
import matplotlib.pyplot as plt
def fx(x):
    return np.exp(-x)-x

def gx(x):
    return np.exp(-x) 
tolerancia=0.0001
xi=0
error=np.abs(gx(xi)-xi)
i=0
while(error>tolerancia and i<=100):
    print(i,'         xi=',xi,'         f(xi)=',fx(xi),'       g(xi)=',gx(xi),'     error V=',error)  
    if i >0:
      error=np.abs(gx(xi)-xi)
    xi=gx(xi)
    i=i+1
print('el valor de x, tal que f(x)=0 es :',xi)    
    
x=np.linspace(0,1.5,100)
plt.title('metodo de punto fijo')    
plt.plot(x,fx(x),label='f(x)')
plt.plot(x,gx(x),label='g(x')
plt.plot(x,x,label='f(x)=x')
plt.axvline(xi,label=f"f(x)=0,  x={xi:.6f}",color='k')
plt.axhline(0,color='k')
plt.legend(loc='upper right')
plt.grid()
plt.show()
