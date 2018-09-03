# -*- coding: utf-8 -*-
"""
Created on Mon Sep 03 12:37:21 2018

@author: Estudiantes
"""

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

matrizOriginal = (io.imread('blackWhite.png')/255.0)/255.0
i, j = matrizOriginal.shape

subMatrices = []
subMaHor = []

for x in range(i/160):
    for y in range(j/61):
        subMatrices.append(matrizOriginal[(x*160):160*(x+1),(y*61):61*(y+1)])
    
for n in range(j/61):
    subMaHor.append(np.concatenate(subMatrices[n*7:(n+1)*7], axis=0))
    

plt.imshow(matrizOriginal, vmin=0, vmax=1)
plt.figure()
plt.imshow(matrizAleatoria, vmin=0, vmax=1)
