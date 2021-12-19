# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:06:34 2020

@author: kadir
"""

import numpy as np
import random
from numba import jit

def findones(Mat):
    vec = []
    for row in Mat:
        vec.append(list(row).count(1))
    return vec

def myProgram():
    NList = np.arange(2, 101, 2)
    maxIndexList = []
    
    for N in NList:
        M = np.zeros(N*N).reshape(N, N)
        
        for i in range(N):
            i = random.randint(0, N - 1)
            j = random.randint(0, N - 1)
            
            while M[i, j] == 1:
                i = random.randint(0, N - 1)
                j = random.randint(0, N - 1)
                
            M[i, j] = 1
            
        v = findones(M)
        
        maxIndexList.append(v.index(max(v)))
    
    return maxIndexList

iterate = 30000

maxIndexListAverage = myProgram()

for i in range(iterate):
    tempList = myProgram()
    
    for j in range(len(tempList)):
        maxIndexListAverage[j] = (maxIndexListAverage[j] * (i + 1) + tempList[j]) / (i + 2)
        
print(maxIndexListAverage)