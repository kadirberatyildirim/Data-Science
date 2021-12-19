
import numpy as np

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
      
    entries1 = print("Enter the entries in a single line (separated by space): ") 
    
    # User input of entries in a  
    # single line separated by space
    entries = list(map(int, input().split())) 
    
    # For printing the matrix 
    matrix = np.array(entries).reshape(R, C) 
    return matrix

matrix = createMatrix()

n = int(input('What is the maximum number of tries for nilpotency? '))

nilpo(matrix, n)
