# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 18:54:12 2018

@author: FamiliaHogar
"""

from random import shuffle
from random import choice
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['image.cmap'] = 'gray'

matrizOriginal = (io.imread('blackWhite.png')/255.0)/255.0
i, j = matrizOriginal.shape

subMatrices = []
divHor = []
divVer = []

for n in range(2, 11):
    if (i % n) == 0:
        divVer.append(n)

for m in range(2, 11):
    if (j % m) == 0:
        divHor.append(m)

nPartVer = choice(divVer)
nPartHor = choice(divHor)

for x in range(nPartVer):
    for y in range(nPartHor):
        subMatrices.append(matrizOriginal[(x*int(i/nPartVer)):(int(i/nPartVer)*(x+1)),
                                          (y*int(j/nPartHor)):(int(j/nPartHor)*(y+1))])

shuffle(subMatrices)
imaRand = np.hstack((subMatrices[0:nPartHor]))

for p in range(1, nPartVer):
    imaRand = np.concatenate((imaRand, np.hstack((subMatrices[(p*nPartHor):((p+1)*nPartHor)]))),
                             axis=0)

plt.imshow(matrizOriginal, vmin=0, vmax=1)
plt.figure()
plt.imshow(imaRand, vmin=0, vmax=1)

io.imsave("imagenAleatoria.png", imaRand)

