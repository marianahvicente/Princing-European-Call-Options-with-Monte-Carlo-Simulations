# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:29:14 2026

@author: HP
"""

"""SIMPLE EXAMPLE ON HOW TO
BUILD A LIST WITH A FUNCTION
USING PREVIOUS OUTPUTS AS INPUTS 


Sn=1
St=[Sn]
    

def stock_price(Sn):
    Sn1=Sn+1
    St.append(Sn1)
    return Sn1
    
    
for i in range(5):
    Sn=stock_price(Sn)
    

print(Sn)
print(St)
"""
'''
#For our case

import numpy as np
rng = np.random.default_rng()
rng

#sanity check
numbers = rng.normal(size=100000000)
numbers.mean()
numbers.std()

t=np.linspace(0, 1000,1001)
r=0.03
vol=0.2
Sn=25
dt=1
St=[Sn]


def stock_price(Sn):
    Sn1=Sn+r*Sn*dt+vol*Sn*rng.normal()
    St.append(Sn1)
    return Sn1
    
    
for i in range(1000):
    Sn=stock_price(Sn)
    
print(Sn)
print(St)

import matplotlib.pyplot as plt
plt.plot(t,St)

print(St)

print(Sn)

#I DID IT FOR ONE SIMULATION!!! Now, how to represent multiple in a graph?


t=np.linspace(0, 1000,1001)
r=0.03
vol=0.2
Sn=25
dt=1
St_b=[Sn]


def stock_price(Sn):
    Sn1=Sn+r*Sn*dt+vol*Sn*rng.normal()
    St_b.append(Sn1)
    return Sn1
    
    
for i in range(1000):
    Sn=stock_price(Sn)
    
import matplotlib.pyplot as plt
plt.plot(t,St, St_b)

#Okay, I know how to do it for 2, but I need like 1000 simulations... 
import matplotlib.pyplot as plt

t=np.linspace(0, 1000,1001)
r=0.03
vol=0.2
Sn=25
dt=1


def stock_price(Sn):
    Sn1=Sn+r*Sn*dt+vol*Sn*rng.normal()
    St.append(Sn1)
    return Sn1
    
for sim in range(1000):    #in this way this does this 1000 times 
    Sn=25
    St=[Sn]
    for i in range(1000):   #And this 1000 times
        Sn=stock_price(Sn)
    plt.plot(t,St)
'''
#Doneee! But now I want to focus only on ST (the values at maturity) 
#How can I do it?

""" just to test
test=[1,2,3]
test[-1]
"""
import numpy as np
rng = np.random.default_rng()
rng

import matplotlib.pyplot as plt


T=100
t=np.linspace(0,T,101)
r=0.03
vol=0.2
Sn=25
dt=1
K=40


def stock_price(Sn):
    Sn1=Sn+r*Sn*dt+vol*Sn*rng.normal()
    St.append(Sn1)
    return Sn1

ST=[]
for sim in range(25000):    
    Sn=25
    St=[Sn]
    for i in range(100):
        Sn=stock_price(Sn)
    plt.plot(t,St)
    plt.xlabel('Time')
    plt.ylabel('St')
    ST.append(St[-1])
    
print(ST)
payoff=[max(x-K,0) for x in ST]

Exp_Payoffs=[1/len(payoff)*x for x in payoff]
V0=(np.exp(-r*T))*sum(Exp_Payoffs)
print(V0)



#Sanity check with Black- Scholes
import numpy as np
from scipy.stats import norm

N = norm.cdf

def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r*T)* N(d2)

BS_CALL(25,40,100,0.03,0.2)


#OKAY, It looks like it is finnaly making sense, and the value corresponds to the one giben by Black-Scholes
