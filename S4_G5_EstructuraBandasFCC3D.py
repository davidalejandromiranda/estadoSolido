#!/usr/bin/env python
# coding: utf-8

# In[7]:

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as cte

a = 1

pi = np.pi
b  = 2*pi/a


b1 = np.r_[b, b, -b]
b2 = np.r_[b, -b, b]
b3 = np.r_[-b, b, b]



k_Gamma = np.r_[0   , 0 , 0]
k_L     = np.r_[b/2 , b/2 , b/2]
k_X     = np.r_[b , 0 , 0] 
k_K     = np.r_[3*b/4, 3*b/4, 0]
k_U     = np.r_[b, b/4, b/4]
k_W     = np.r_[b, b/2, 0,]    

hbar = cte.hbar/cte.e # eV s
m_e  = cte.m_e


e_f  = (2*hbar*(b**2))/2*m_e*2*pi

def energy(k1, k2,  m1 = 0, m2 = 0, m3 = 0, number_of_k_points = 1000): #añador el m3 para 3D
    k_12 = k2 - k1 
    norm_k_12 = np.linalg.norm(k_12) #Funcion para calcular la norma.
    uk_12 = k_12 / norm_k_12 #vector unitario en dirección 1,2.
    X = np.linspace(0, norm_k_12, number_of_k_points) # definir los numeros. arranco en 0 y se termina en el tamañano que se dio de GAMMA y X
    K = [ k1 + x*uk_12 + m1*b1 + m2*b2 + m3*b3  for x in X ] # nos da como resultado un vector. K=K1+xUk_12
    E = [ hbar**2 * np.dot(k,k) / (2*m_e) for k in K]#calculo de la energía . np.dot (k,k)
    return X, np.array(E) #devolver las energías

k_path = [k_L, k_K, k_U, k_W, k_Gamma, k_X, k_W, k_L, k_Gamma,k_K, k_U, k_X]
k_labels = [r'$L$', r'$K$', r'$U$', r'$W$', r'$\Gamma$',r'$X$', r'$W$', r'$L$', r'$\Gamma$'r'$K$', r'$U$', r'$X$']

plt.figure(dpi = 200)
BZ = { # valores de m1 y m2 para la BZ -> (m1, m2)
    
    1: ( 0,  0, 0), #la que esta en el centro. #MIRAR PAG 74
    2: (-1,  0, 0), #INDICES DE LA CELDA UNITARIA, LO QUE HACEES DENOTAR LAS ZONAS.
    3: ( 0, -1, 0),
    4: ( 0,  0,-1),
    5: (-1, -1,-1),
    6: ( 1,  0, 0),
    7: ( 0,  1, 0),
    8: ( 0,  0, 1),
    9: ( 1,  1, 1),
    10: ( 1,  1,-1),
    11: ( 1,  1, 1),
    12: (-1,  1, 1),
    13: ( 1,  1, 0),
    14: ( 1,  0, 1),
    15: ( 0,  1, 1),
    16: (-1, -1, 1),
    17: (-1,  1,-1),
    18: ( 1, -1,-1),
    19: (-1, -1, 0),
    20: (-1,  0,-1),
    21: ( 0, -1,-1),
    22: ( 1, -1, 0),
    23: ( 1,  0,-1),
    24: (-1,  1, 0),
    25: (-1,  0, 1),
    26: ( 0, -1, 1),
    27: ( 0,  1,-1)}

z_index = []
for zone in range(1, 28):
    m1 = BZ[zone][0] #RECORRER LAS ZONAS
    m2 = BZ[zone][1]
    m3 = BZ[zone][2]
    Dk = 0
    
            
    for i in range(len(k_path)-1):#Longitud del camino, en este caso es 5.
        k, E = energy(k_path[i], k_path[i+1], m1 = m1, m2 = m2, m3=m3)
        k += Dk # k, inicializo en cero, arranca desde el ultimo valor. 
        plt.plot(k, E-e_f , 'k', lw = 1)
        Dk = k.max() #valor mas grade de k 
        
    plt.ylim(-10, 30)
    plt.xlim(0, 50)
    
    plt.xlabel(r'$\vec{k}$')
    plt.ylabel(r'$E_{\vec{k}}$ [eV]')


# In[ ]:





# In[ ]:




