# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 12:58:20 2018

@author: FamiliaHogar
"""
import numpy as np

matrizOriginal = np.random.randint(0, 99, (30,30))
matrizSuavizada = np.zeros((30,30))
#print(matrizOriginal)

for x in range(30):
    for y in range(30):                
        matrizSuavizada[x,y] = ((matrizOriginal[(x+1)%10,y] + matrizOriginal[(x+1)%10,(y+1)%10] 
        + matrizOriginal[x,(y+1)%10] + matrizOriginal[x-1,(y+1)%10] + matrizOriginal[x-1,y] 
        + matrizOriginal[x-1,y-1] + matrizOriginal[x,y-1] + matrizOriginal[(x+1)%10,y-1] 
        + matrizOriginal[x,y])/10)
        
        