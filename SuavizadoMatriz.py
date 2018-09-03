# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 12:58:20 2018

@author: FamiliaHogar
"""
import numpy as np
import matplotlib.pyplot as plt

###### Ejercicio original ######

matrizOriginal = np.random.randint(0, 99, (30,30))
matrizSuavizada = np.zeros((30,30))

for x in range(30):
    for y in range(30):                
        matrizSuavizada[x,y] = ((matrizOriginal[(x+1)%30,y] + matrizOriginal[(x+1)%30,(y+1)%30] 
        + matrizOriginal[x,(y+1)%30] + matrizOriginal[x-1,(y+1)%30] + matrizOriginal[x-1,y] 
        + matrizOriginal[x-1,y-1] + matrizOriginal[x,y-1] + matrizOriginal[(x+1)%30,y-1] 
        + matrizOriginal[x,y])/10)
        
###### Matriz con cuadros en las esquinas ######
        
plt.rcParams['image.cmap'] = 'gray'

matrizOriginal = np.zeros((30, 30))
for x in range(30):
    for y in range(30):
        if (y > 10 or x < 20) and (x > 10 or y < 20):
            matrizOriginal[x,y] = 1

###### Matriz con un cuadro en la mitad #######

matrizOriginal = np.zeros((30, 30))
for x in range(30):
    for y in range(30):
        if (y > 5 and x > 5) and (x < 25 and y < 25):
            matrizOriginal[x,y] = 1
        
###### Matriz continua en los bordes ######

matrizOriginal = np.random.random((30,30))
matrizSuavizada = np.zeros((30, 30))

for x in range(30):
    for y in range(30):                
        matrizSuavizada[x,y] = ((matrizOriginal[(x+1)%30,y] + matrizOriginal[(x+1)%30,(y+1)%30] 
        + matrizOriginal[x,(y+1)%30] + matrizOriginal[x-1,(y+1)%30] + matrizOriginal[x-1,y] 
        + matrizOriginal[x-1,y-1] + matrizOriginal[x,y-1] + matrizOriginal[(x+1)%30,y-1] 
        + matrizOriginal[x,y])/10)

plt.imshow(matrizOriginal, vmin=0, vmax=1)
plt.figure()
plt.imshow(matrizSuavizada,vmin=0,vmax=1)

###### Bordes repetidos ######

matrizOriginal = np.random.randint(0, 99, (32,32))
matrizSuavizadaBord = np.zeros((32, 32))
matrizSuavizada = np.zeros((30, 30))

for x in range(1):
    for y in range(32):
        matrizOriginal[x,y] = matrizOriginal[x+1,y]
        
for x in range(32):
    for y in range(1):
        matrizOriginal[x,y] = matrizOriginal[x,y+1]

for x in range(32):
    for y in range(31,32):
        matrizOriginal[x,y] = matrizOriginal[x,y-1]
        
for x in range(31,32):
    for y in range(32):
        matrizOriginal[x,y] = matrizOriginal[x-1,y]

for x in range(1,31):
    for y in range(1,31):                
        matrizSuavizadaBord[x,y] = ((matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y+1)] 
        + matrizOriginal[x,(y+1)] + matrizOriginal[x-1,(y+1)] + matrizOriginal[x-1,y] 
        + matrizOriginal[x-1,y-1] + matrizOriginal[x,y-1] + matrizOriginal[(x+1),y-1] 
        + matrizOriginal[x,y])/10)
        
for x in range(30):
    for y in range(30):
        matrizSuavizada[x,y] = matrizSuavizadaBord[x+1,y+1]
        
        