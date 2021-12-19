from matplotlib import pyplot as plt

from matplotlib import animation
import numpy as np

fig = plt.figure()

x = ['S','I','R']

S = [0.99]
I = [0.01]
R = [0.0]
a=0.7
b=0.2

for t in range(50):
    S.append(S[t]-a*I[t]*S[t])
    I.append(I[t]+a*I[t]*S[t]-b*I[t])
    R.append(R[t]+b*I[t])

data = np.transpose([S,I,R])

rects = plt.bar(x, data[0], color=['b','r','g'])
#line, = plt.plot(x, data[0], color='r')
plt.ylim(0, 1)
def animate(i):
    for rect, yi in zip(rects, data[i]):
        rect.set_height(yi)
    return rects

anim = animation.FuncAnimation(fig, animate, frames=len(data), interval=100)
plt.show()
