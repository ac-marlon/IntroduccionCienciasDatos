# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 18:54:12 2018

@author: FamiliaHogar
"""

from random import shuffle
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['image.cmap'] = 'gray'

matrizOriginal = (io.imread('blackWhite.png')/255.0)/255.0
i, j = matrizOriginal.shape

subMatrices = []

for x in range(4):
    for y in range(7):
        subMatrices.append(matrizOriginal[(x*160):160*(x+1), (y*61):61*(y+1)])

shuffle(subMatrices)

imaRand = np.vstack((np.hstack((subMatrices[0:7])),
                     np.hstack((subMatrices[7:14])),
                     np.hstack((subMatrices[14:21])),
                     np.hstack((subMatrices[21:28]))))

plt.imshow(matrizOriginal, vmin=0, vmax=1)
plt.figure()
plt.imshow(imaRand, vmin=0, vmax=1)

io.imsave("imagenAleatoria.png", imaRand)
