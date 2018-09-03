# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 12:32:52 2018

@author: FamiliaHogar
"""
import matplotlib.pyplot as plt
import numpy as np
from skimage import io

plt.rcParams['image.cmap'] = 'gray'
size=(20,30)

imagen_negra = np.zeros(size)
imagen_blanca = np.ones(size)
imagen_gris = np.ones(size)*0.5
imagen_aleatoria = np.random.rand(size[0],size[1])
imagen_gradiente = np.linspace(0, 1, 600).reshape(20,30)

#Test:
matrizOriginal = np.random.random((30,30))
matrizSuavizada = np.zeros((30, 30))

for x in range(30):
    for y in range(30):                
        matrizSuavizada[x,y] = ((matrizOriginal[(x+1)%30,y] + matrizOriginal[(x+1)%30,(y+1)%30] 
        + matrizOriginal[x,(y+1)%30] + matrizOriginal[x-1,(y+1)%30] + matrizOriginal[x-1,y] 
        + matrizOriginal[x-1,y-1] + matrizOriginal[x,y-1] + matrizOriginal[(x+1)%30,y-1] 
        + matrizOriginal[x,y])/10)

#plt.imshow(imagen_negra,vmin=0,vmax=1)
#plt.figure()
#plt.imshow(imagen_blanca,vmin=0,vmax=1)
#plt.figure()
#plt.imshow(imagen_gris,vmin=0,vmax=1)
#plt.figure()
plt.imshow(imagen_aleatoria,vmin=0,vmax=1)
plt.figure()
plt.imshow(imagen_gradiente,vmin=0,vmax=1)
plt.figure()
plt.imshow(matrizOriginal,vmin=0,vmax=1)
plt.figure()
plt.imshow(matrizSuavizada,vmin=0,vmax=1)

io.imsave("matrizOriginal.png", matrizOriginal)
io.imsave("matrizSuavizada.png", matrizSuavizada)
