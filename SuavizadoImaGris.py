# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 12:58:20 2018

@author: FamiliaHogar
"""
import matplotlib.pyplot as plt
from skimage import io

#Carga de imagenes en escala de grises:

grayGirl=io.imread("imaTestGris.jpg")/255.0

print("- Dimensiones de la imagen:")
print(grayGirl.shape)
plt.imshow(grayGirl,vmin=0,vmax=1)

#Carga de imagenes a color:
plt.figure()

colorGirl=io.imread("imaTestColor.jpg")/255.0

print("- Dimensiones de la imagen:")
print(colorGirl.shape)
plt.imshow(colorGirl,vmin=0,vmax=1)


plt.imshow(lena_rgb[:,:,0],vmin=0,vmax=1)
plt.title("Canal Rojo")
plt.figure()
plt.imshow(lena_rgb[:,:,1],vmin=0,vmax=1)
plt.title("Canal Verde")
plt.figure()
plt.imshow(lena_rgb[:,:,2],vmin=0,vmax=1)
plt.title("Canal Azul")

