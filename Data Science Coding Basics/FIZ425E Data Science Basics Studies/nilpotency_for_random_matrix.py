
import numpy as np
import random

def checkzero(matrix):
    return False if np.count_nonzero(matrix) != 0 else True        

def matrixpower(matrix, p):
     return np.linalg.matrix_power(matrix, p)

def nilpo(matrix, n):
    for p in range(2, n):
        if checkzero(matrixpower(matrix, p)) == True:
            print('Found p: ', p)
            break
        if p == n-1:
            print('Seems like this matrix is not nilpotent')

def createMatrix():
    R = int(input("Enter the number of rows: ")) 
    C = int(input("Enter the number of columns: "))

    matrix = np.triu(np.array([random.randint(1, 999) for _ in range (R**2)]).reshape(R, C), k=1)
    print(matrix)
    return matrix

matrix = createMatrix()

n = int(input('What is the maximum number of tries for nilpotency? '))

nilpo(matrix, n)
