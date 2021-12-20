import numpy as np

x = np.arange(6)
print('original array')
print(x)
"""
assert command is used to make program test the condition given to it
if the condition is false, program raises an assertionError
this method can be used to detect problems early
"""
r1 = np.mean(x)
r2 = np.average(x)
assert np.allclose(r1, r2)
print('Mean: ', r1)

r1 = np.std(x)
r2 = np.sqrt(np.mean((x - np.mean(x)) ** 2 ))
assert np.allclose(r1, r2)
print('std: ', r1)

r1 = np.var(x)
r2 = np.mean((x - np.mean(x)) ** 2 )
assert np.allclose(r1, r2)
print('var: ', r1)

