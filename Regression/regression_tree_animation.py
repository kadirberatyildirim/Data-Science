import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#===================================================Create Data
def f(x):
    mu, sigma = 0, 1.5
    return -x**2 + x + 5 + np.random.normal(mu, sigma, 1)

np.random.seed(1)
    
x = np.random.uniform(-2, 5, 300)
y = np.array( [f(i) for i in x] )

p = x.argsort()
x = x[p]
y = y[p]


#===================================================Calculate Thresholds
def SSR(r, y): #send numpy array
    return np.sum( (r - y)**2 )

SSRs, thresholds = [], []
for i in range(len(x) - 1):
    threshold = x[i:i+2].mean()
    
    low = np.take(y, np.where(x < threshold))
    high = np.take(y, np.where(x > threshold))
    
    guess_low = low.mean()
    guess_high = high.mean()
    
    SSRs.append(SSR(low, guess_low) + SSR(high, guess_high))
    thresholds.append(threshold)

#===================================================Animated Plot
fig, (ax1, ax2) = plt.subplots(2,1, sharex = True)
x_data, y_data = [], []
x_data2, y_data2 = [], []
ln, = ax1.plot([], [], 'r--')
ln2, = ax2.plot(thresholds, SSRs, 'ro', markersize = 2)
line = [ln, ln2]

def init():
    ax1.scatter(x, y, s = 3)
    ax1.title.set_text('Trying Different Thresholds')
    ax2.title.set_text('Threshold vs SSR')
    ax1.set_ylabel('y values')
    ax2.set_xlabel('Threshold')
    ax2.set_ylabel('SSR')
    return line

def update(frame):
    x_data = [x[frame:frame+2].mean()] * 2
    y_data = [min(y), max(y)]
    line[0].set_data(x_data, y_data)

    x_data2.append(thresholds[frame])
    y_data2.append(SSRs[frame])
    line[1].set_data(x_data2, y_data2)
    return line

ani = FuncAnimation(fig, update, frames = 298,
                    init_func = init, blit = True)
plt.show()
#ani.save('regression_tree_thresholds_120.gif', writer='imagemagick', fps=120)