# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 12:18:00 2018

@author: FamiliaHogar
"""

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

matrizOriginal = np.random.random((30,30))
matrizSuavizada = np.zeros((30, 30))

for x in range(30):
    for y in range(30):                
        matrizSuavizada[x,y] = ((matrizOriginal[(x+1)%30,y] + matrizOriginal[(x+1)%30,(y+1)%30] 
        + matrizOriginal[x,(y+1)%30] + matrizOriginal[x-1,(y+1)%30] + matrizOriginal[x-1,y] 
        + matrizOriginal[x-1,y-1] + matrizOriginal[x,y-1] + matrizOriginal[(x+1)%30,y-1] 
        + matrizOriginal[x,y])/10)

#plt.imshow(matrizOriginal, vmin=0, vmax=1)
#plt.figure()
#plt.imshow(matrizSuavizada,vmin=0,vmax=1)
#plt.figure()

arrayMujerModelo = io.imread('mujer.jpg')/255.0

h,w,c = arrayMujerModelo.shape # obtenemos el tamaño de la imagen original
mujerGris = np.zeros((h,w)) # creamos una matriz donde generar la imagen

plt.imshow(arrayMujerModelo,vmin=0,vmax=1)
plt.title("Dimensiones de la imagen: \n" + str(arrayMujerModelo.shape))

#Se promedia el RGB y se asigna al pixel i,j de la imagen final en grises
for i in range(h):
    for j in range(w):
        mujerGris[i,j] = (arrayMujerModelo[i,j,0] + arrayMujerModelo[i,j,1] + arrayMujerModelo[i,j,2])/3

plt.figure()
plt.imshow(mujerGris,vmin=0,vmax=1)   
plt.title("Dimensiones de la imagen: \n" + str(mujerGris.shape))

io.imsave("blackWhite.png", mujerGris)