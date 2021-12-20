
import numpy as np
import matplotlib.pyplot as plt

mu = 5
sigma = 2

values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
plt.show()