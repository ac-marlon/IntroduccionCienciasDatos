# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 14:12:49 2018

@author: FamiliaHogar
"""

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['image.cmap'] = 'gray'
matrizOriginal = (io.imread('blackWhite.png')/255.0)/255.0
i, j = matrizOriginal.shape
matrizSuavizada = np.zeros((i, j))
matrizBordeada = np.zeros((i, j))
matrizPerfilada = np.zeros((i, j))

###### Suavizado ######

for x in range(i):
    for y in range(j): 
        if x == 0 and y == 0:
            matrizSuavizada[x,y] = ((matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y+1)] 
            + matrizOriginal[x,(y+1)] + matrizOriginal[x,(y+1)] + matrizOriginal[x,y] 
            + matrizOriginal[x,y] + matrizOriginal[x,y] + matrizOriginal[(x+1),y] 
            + matrizOriginal[x,y])/10)
        elif x == i-1 and y == 0:
            matrizSuavizada[x,y] = ((matrizOriginal[(x),y] + matrizOriginal[(x),(y+1)] 
            + matrizOriginal[x,(y+1)] + matrizOriginal[x-1,(y+1)] + matrizOriginal[x-1,y] 
            + matrizOriginal[x-1,y] + matrizOriginal[x,y] + matrizOriginal[(x),y] 
            + matrizOriginal[x,y])/10)
        elif x == i-1 and y == j-1:
            matrizSuavizada[x,y] = ((matrizOriginal[(x),y] + matrizOriginal[(x),(y)] 
            + matrizOriginal[x,(y)] + matrizOriginal[x-1,(y)] + matrizOriginal[x-1,y] 
            + matrizOriginal[x-1,y-1] + matrizOriginal[x,y-1] + matrizOriginal[(x),y-1] 
            + matrizOriginal[x,y])/10)
        elif x == 0 and y == j-1:
            matrizSuavizada[x,y] = ((matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y)] 
            + matrizOriginal[x,(y)] + matrizOriginal[x,(y)] + matrizOriginal[x,y] 
            + matrizOriginal[x,y-1] + matrizOriginal[x,y-1] + matrizOriginal[(x+1),y-1] 
            + matrizOriginal[x,y])/10)
        elif y == 0 and x != 0 and x != i-1: 
            matrizSuavizada[x,y] = ((matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y+1)] 
            + matrizOriginal[x,(y+1)] + matrizOriginal[x-1,(y+1)] + matrizOriginal[x-1,y] 
            + matrizOriginal[x-1,y] + matrizOriginal[x,y] + matrizOriginal[(x+1),y] 
            + matrizOriginal[x,y])/10)
        elif x == i-1 and y != 0 and y != j-1:
            matrizSuavizada[x,y] = ((matrizOriginal[(x),y] + matrizOriginal[(x),(y+1)] 
            + matrizOriginal[x,(y+1)] + matrizOriginal[x-1,(y+1)] + matrizOriginal[x-1,y] 
            + matrizOriginal[x-1,y-1] + matrizOriginal[x,y-1] + matrizOriginal[(x),y-1] 
            + matrizOriginal[x,y])/10)
        elif y == j-1 and x != 0 and x != i-1:
            matrizSuavizada[x,y] = ((matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y)] 
            + matrizOriginal[x,(y)] + matrizOriginal[x-1,(y)] + matrizOriginal[x-1,y] 
            + matrizOriginal[x-1,y-1] + matrizOriginal[x,y-1] + matrizOriginal[(x+1),y-1] 
            + matrizOriginal[x,y])/10)
        elif x == 0 and y != 0 and y != j-1:
            matrizSuavizada[x,y] = ((matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y+1)] 
            + matrizOriginal[x,(y+1)] + matrizOriginal[x,(y+1)] + matrizOriginal[x,y] 
            + matrizOriginal[x,y-1] + matrizOriginal[x,y-1] + matrizOriginal[(x+1),y-1] 
            + matrizOriginal[x,y])/10)
        else:
            matrizSuavizada[x,y] = ((matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y+1)] 
            + matrizOriginal[x,(y+1)] + matrizOriginal[x-1,(y+1)] + matrizOriginal[x-1,y] 
            + matrizOriginal[x-1,y-1] + matrizOriginal[x,y-1] + matrizOriginal[(x+1),y-1] 
            + matrizOriginal[x,y])/10)
            
###### Bordes ######
            
for x in range(i):
    for y in range(j): 
        if x == 0 and y == 0:
            matrizBordeada[x,y] = ((2*matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y+1)] 
            - matrizOriginal[x,(y+1)] - 2*matrizOriginal[x,y] 
            - matrizOriginal[x,y] + matrizOriginal[(x+1),y])/4)
        elif x == i-1 and y == 0:
            matrizBordeada[x,y] = ((2*matrizOriginal[(x),y] + matrizOriginal[(x),(y+1)] 
            - matrizOriginal[x-1,(y+1)] - 2*matrizOriginal[x-1,y] 
            - matrizOriginal[x-1,y] + matrizOriginal[(x),y])/4)
        elif x == i-1 and y == j-1:
            matrizBordeada[x,y] = ((2*matrizOriginal[(x),y] + matrizOriginal[(x),(y)] 
            - matrizOriginal[x-1,(y)] - 2*matrizOriginal[x-1,y] 
            - matrizOriginal[x-1,y-1] + matrizOriginal[(x),y-1])/4)
        elif x == 0 and y == j-1:
            matrizBordeada[x,y] = ((2*matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y)] 
            - matrizOriginal[x,(y)] - 2*matrizOriginal[x,y] 
            - matrizOriginal[x,y-1] + matrizOriginal[(x+1),y-1])/4)
        elif y == 0 and x != 0 and x != i-1: 
            matrizBordeada[x,y] = ((2*matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y+1)] 
            - matrizOriginal[x-1,(y+1)] - 2*matrizOriginal[x-1,y] 
            - matrizOriginal[x-1,y] + matrizOriginal[(x+1),y])/4)
        elif x == i-1 and y != 0 and y != j-1:
            matrizBordeada[x,y] = ((2*matrizOriginal[(x),y] + matrizOriginal[(x),(y+1)] 
            - matrizOriginal[x-1,(y+1)] - 2*matrizOriginal[x-1,y] 
            - matrizOriginal[x-1,y-1] + matrizOriginal[(x),y-1])/4)
        elif y == j-1 and x != 0 and x != i-1:
            matrizBordeada[x,y] = ((2*matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y)] 
            - matrizOriginal[x-1,(y)] - 2*matrizOriginal[x-1,y] 
            - matrizOriginal[x-1,y-1] + matrizOriginal[(x+1),y-1])/4)
        elif x == 0 and y != 0 and y != j-1:
            matrizBordeada[x,y] = ((2*matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y+1)] 
            - matrizOriginal[x,(y+1)] - 2*matrizOriginal[x,y] 
            - matrizOriginal[x,y-1] + matrizOriginal[(x+1),y-1])/4)
        else:
            matrizBordeada[x,y] = ((2*matrizOriginal[(x+1),y] + matrizOriginal[(x+1),(y+1)] 
            - matrizOriginal[x-1,(y+1)] - 2*matrizOriginal[x-1,y] 
            - matrizOriginal[x-1,y-1] + matrizOriginal[(x+1),y-1])/4)
            
###### Perfilado ######
            
for x in range(i):
    for y in range(j): 
        if x == 0 and y == 0:
            matrizPerfilada[x,y] = ((-matrizOriginal[(x+1),y] - matrizOriginal[(x+1),(y+1)] 
            - matrizOriginal[x,(y+1)] - matrizOriginal[x,(y+1)] - matrizOriginal[x,y] 
            - matrizOriginal[x,y] - matrizOriginal[x,y] - matrizOriginal[(x+1),y] 
            + 9*matrizOriginal[x,y])/6)
        elif x == i-1 and y == 0:
            matrizPerfilada[x,y] = ((-matrizOriginal[(x),y] - matrizOriginal[(x),(y+1)] 
            - matrizOriginal[x,(y+1)] - matrizOriginal[x-1,(y+1)] - matrizOriginal[x-1,y] 
            - matrizOriginal[x-1,y] - matrizOriginal[x,y] - matrizOriginal[(x),y] 
            + 9*matrizOriginal[x,y])/6)
        elif x == i-1 and y == j-1:
            matrizPerfilada[x,y] = ((-matrizOriginal[(x),y] - matrizOriginal[(x),(y)] 
            - matrizOriginal[x,(y)] - matrizOriginal[x-1,(y)] - matrizOriginal[x-1,y] 
            - matrizOriginal[x-1,y-1] - matrizOriginal[x,y-1] - matrizOriginal[(x),y-1] 
            + 9*matrizOriginal[x,y])/6)
        elif x == 0 and y == j-1:
            matrizPerfilada[x,y] = ((-matrizOriginal[(x+1),y] - matrizOriginal[(x+1),(y)] 
            - matrizOriginal[x,(y)] - matrizOriginal[x,(y)] - matrizOriginal[x,y] 
            - matrizOriginal[x,y-1] - matrizOriginal[x,y-1] - matrizOriginal[(x+1),y-1] 
            + 9*matrizOriginal[x,y])/6)
        elif y == 0 and x != 0 and x != i-1: 
            matrizPerfilada[x,y] = ((-matrizOriginal[(x+1),y] - matrizOriginal[(x+1),(y+1)] 
            - matrizOriginal[x,(y+1)] - matrizOriginal[x-1,(y+1)] - matrizOriginal[x-1,y] 
            - matrizOriginal[x-1,y] - matrizOriginal[x,y] - matrizOriginal[(x+1),y] 
            + 9*matrizOriginal[x,y])/6)
        elif x == i-1 and y != 0 and y != j-1:
            matrizPerfilada[x,y] = ((-matrizOriginal[(x),y] - matrizOriginal[(x),(y+1)] 
            - matrizOriginal[x,(y+1)] - matrizOriginal[x-1,(y+1)] - matrizOriginal[x-1,y] 
            - matrizOriginal[x-1,y-1] - matrizOriginal[x,y-1] - matrizOriginal[(x),y-1] 
            + 9*matrizOriginal[x,y])/6)
        elif y == j-1 and x != 0 and x != i-1:
            matrizPerfilada[x,y] = ((-matrizOriginal[(x+1),y] - matrizOriginal[(x+1),(y)] 
            - matrizOriginal[x,(y)] - matrizOriginal[x-1,(y)] - matrizOriginal[x-1,y] 
            - matrizOriginal[x-1,y-1] - matrizOriginal[x,y-1] - matrizOriginal[(x+1),y-1] 
            + 9*matrizOriginal[x,y])/6)
        elif x == 0 and y != 0 and y != j-1:
            matrizPerfilada[x,y] = ((-matrizOriginal[(x+1),y] - matrizOriginal[(x+1),(y+1)] 
            - matrizOriginal[x,(y+1)] - matrizOriginal[x,(y+1)] - matrizOriginal[x,y] 
            - matrizOriginal[x,y-1] - matrizOriginal[x,y-1] - matrizOriginal[(x+1),y-1] 
            + 9*matrizOriginal[x,y])/6)
        else:
            matrizPerfilada[x,y] = ((-matrizOriginal[(x+1),y] - matrizOriginal[(x+1),(y+1)] 
            - matrizOriginal[x,(y+1)] - matrizOriginal[x-1,(y+1)] - matrizOriginal[x-1,y] 
            - matrizOriginal[x-1,y-1] - matrizOriginal[x,y-1] - matrizOriginal[(x+1),y-1] 
            + 9*matrizOriginal[x,y])/6)

plt.imshow(matrizOriginal,vmin=0,vmax=1)
plt.figure()
plt.imshow(matrizSuavizada,vmin=0,vmax=1)
plt.figure()
plt.imshow(matrizBordeada,vmin=0,vmax=1)
plt.figure()
plt.imshow(matrizPerfilada,vmin=0,vmax=1)
io.imsave("blackWhiteSuave.png", matrizSuavizada)
io.imsave("blackWhiteBordes.png", matrizBordeada)
io.imsave("blackWhitePerfil.png", matrizPerfilada)
