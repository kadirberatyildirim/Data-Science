import numpy as np
import random
import matplotlib.pyplot as plt

def myfunction(N):
    vec = np.zeros(N)
    numberoftries = 1
    
    numberoftries += 1
    randInt = random.randint(0, N - 1)
    if randInt == 0:
        vec[randInt] = 1
        vec[randInt + 1] = -1
    elif randInt == N - 1:
        vec[randInt] = 1
        vec[randInt - 1] = -1
    else:
        vec[randInt] = 1
        vec[randInt + 1] = -1
        vec[randInt - 1] = -1
    
    while sum(vec) != 0:
        numberoftries += 1
        randInt = random.randint(0, N - 1)
        if randInt == 0:
            vec[randInt] = 1
            vec[randInt + 1] = -1
        elif randInt == N - 1:
            vec[randInt] = 1
            vec[randInt - 1] = -1
        else:
            vec[randInt] = 1
            vec[randInt + 1] = -1
            vec[randInt - 1] = -1
    return vec, numberoftries

def oneMinusOne(N):
    if N <= 0 or N % 2 != 0:
        print('N should be even and positive!')
    else:
        resultantVec, tries = myfunction(N)
        print('Result: ', resultantVec, 'Number of tries: ', tries)
        return tries
    
Ns = np.linspace(2, 40, 20)
numberOfTriesList = []

for i in list(Ns):
    numberOfTriesList.append(oneMinusOne(int(i)))
    
print('Last list: ', numberOfTriesList)

plt.scatter(Ns, numberOfTriesList)
plt.show()