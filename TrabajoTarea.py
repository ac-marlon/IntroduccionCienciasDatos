# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 18:53:19 2018

@author: FamiliaHogar
"""

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

print("Opciones: \n" + "1. Suavizado \n" + "2. Bordes \n" + "3. Pefilado")
numero = int(input("Elegir: "))

if numero == 1:
    
    matrizOriginal = (io.imread('blackWhite.png')/255.0)/255.0
    i, j = matrizOriginal.shape
    matrizSuavizada = np.zeros((i, j))
    
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
    
    plt.imshow(matrizOriginal,vmin=0,vmax=1)
    plt.figure()
    plt.imshow(matrizSuavizada,vmin=0,vmax=1)
    io.imsave("blackWhiteSuave.png", matrizSuavizada)

elif numero == 2:
    
    matrizOriginal = (io.imread('blackWhite.png')/255.0)/255.0
    i, j = matrizOriginal.shape
    matrizBordeada = np.zeros((i, j))
    
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
    
    plt.imshow(matrizOriginal,vmin=0,vmax=1)
    plt.figure()
    plt.imshow(matrizBordeada,vmin=0,vmax=1)
    io.imsave("blackWhiteBordes.png", matrizBordeada)
    
elif numero == 3:
    
    matrizOriginal = (io.imread('blackWhite.png')/255.0)/255.0
    i, j = matrizOriginal.shape
    matrizPerfilada = np.zeros((i, j))
    
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
    plt.imshow(matrizPerfilada,vmin=0,vmax=1)
    io.imsave("blackWhitePerfil.png", matrizPerfilada)
    
else:
    print("Opcion invalida!")
    