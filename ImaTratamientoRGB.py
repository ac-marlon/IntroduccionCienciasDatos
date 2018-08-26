# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 13:16:20 2018

@author: FamiliaHogar
"""
import matplotlib.pyplot as plt
import numpy as np
import PIL
from skimage import io

colorGirl=io.imread("imaTestColor.jpg")/255.0

print("- Dimensiones de la imagen:")
print(colorGirl.shape)
plt.imshow(colorGirl,vmin=0,vmax=1)
plt.title("RGB")
plt.figure()

plt.imshow(colorGirl[:,:,0],vmin=0,vmax=1)
plt.title("Canal Rojo")
plt.figure()
plt.imshow(colorGirl[:,:,1],vmin=0,vmax=1)
plt.title("Canal Verde")
plt.figure()
plt.imshow(colorGirl[:,:,2],vmin=0,vmax=1)
plt.title("Canal Azul")

plt.figure()
colorGirlRed=np.copy(colorGirl) # creo una copia de la imagen para preservar la original
colorGirlRed[:,:,1]=0 # quito el canal azul
colorGirlRed[:,:,2]=0 # quito el canal verde
plt.title("ColorGirl Canal Rojo")
plt.imshow(colorGirlRed)

#Suavizar imagen gris

plt.figure()
grayGirl=io.imread("imaTestGris.jpg")/255.0

print("- Dimensiones de la imagen:")
print(grayGirl.shape)
plt.imshow(grayGirl,vmin=0,vmax=1)
plt.title("Sin suavizar")

imagen = PIL.Image.open("imaTestGris.jpg").convert("L")
imaMatriz = np.array(imagen)
imaMatrizSuav = np.zeros(imaMatriz.shape)
print(imaMatriz.shape)

for x in range(410):
    for y in range(730):                
        imaMatrizSuav[x,y] = ((imaMatriz[(x+1)%410,y] + imaMatriz[(x+1)%410,(y+1)%730] 
        + imaMatriz[x,(y+1)%730] + imaMatriz[x-1,(y+1)%730] + imaMatriz[x-1,y] 
        + imaMatriz[x-1,y-1] + imaMatriz[x,y-1] + imaMatriz[(x+1)%410,y-1] 
        + imaMatriz[x,y])/10)
        
plt.figure()        
plt.imshow(imaMatrizSuav) 
plt.title("Suavizada") 
        



