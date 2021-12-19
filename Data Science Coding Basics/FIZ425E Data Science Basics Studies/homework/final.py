# -*- coding: utf-8 -*-
"""
Kadir Berat YILDIRIM

last digit: 2, number of tries: 12, startN: 20, endN: 10000, howmany: 30
"""
#---------------------Class------------------------------------
#Imports are as usual, numpy and matplotlib plotting methods and time module
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter
#A class is defined easily as follows.
class MCpiKBY(object):
    def __init__(self, N): #Init method is called whenever an object is being created
        self.N = N #N is created as attribute of object here
    
    def calculationKBY(self): #All methods of a class should take input 'self'
        allPoints = self.N
        inside=0
        #x and y values are created randomly with numpy
        x, y = np.random.rand(allPoints), np.random.rand(allPoints)
        #inside is incremented by 1 for each value that is inside the quarter circle as follows
        inside = np.where((x**2 + y**2)**(0.5) < 1,1,0).sum()
        #Then rest of the calculation is easy as also given in exam pdf
        myappiKBY = 4.0 * (inside / allPoints)
        #All that is left for us is to return
        return myappiKBY
    
    def calculatepiKBY(self, num):
        starttime = perf_counter() #Start to count time
        #Following is a one-liner to sum outcomes of calculationKBY method (called num times)
        #and then divide it to num to get average, other line is just time calculation
        mypiKBY = np.sum([self.calculationKBY() for i in range(num)]) / num
        mytimeKBY = (perf_counter() - starttime) / num #End time calculation here
        #Error calculation is as follows
        myerrorKBY = np.abs((np.pi - mypiKBY) / np.pi * 100)
        #this returns a tuple of three variables as requested by question
        return mypiKBY, myerrorKBY, mytimeKBY
#---------------------Class End------------------------------------

#==========================Main Program================================
#Creating constant variables
numberoftries, startN, endN, howmany = 12, 20, 10000, 30
#Creating nearly equidistant integers using numpy
integers = np.round(np.linspace(startN, endN, howmany)).astype(int)
#Creating objects howmany times using integers created above as their N attribute
myObjects = [MCpiKBY(integers[i]) for i in range(howmany)]
#Now here I get the values but they are in form of tuples
values = [i.calculatepiKBY(numberoftries) for i in myObjects]
#That is why to plot with ease, I divide each value into seperate arrays
pi_values, error_values, time_values = [value[0] for value in values], [value[1] for value in values], [value[2] for value in values]
#======Plot
#This plot tempelate is available in matplotlib documentations Tolga Hocam :)
#Of course I have edited it according to our needs for this exam
#Here I create a figure and subplots as axs
fig, axs = plt.subplots(3, sharex=True)
fig.suptitle('The Results of Kadir Berat YILDIRIM') #Just a title
#We plot each value arrays as follows, notice the color arguement given inside paranthesis
#Also for labels, I have used .set method inside matplotlib.pyplot
axs[0].plot(integers, pi_values, 'x', color = 'r')
axs[0].plot((0, 10000), (np.pi, np.pi), color = 'grey')
axs[0].set_ylabel('$\pi$', rotation = 0) #Sets ylabel but without any rotation
axs[1].plot(integers, time_values, color = 'g')
axs[1].set(ylabel = 'Time(s)') #Sets ylabel with automatic rotation
axs[2].plot(integers, error_values, color = 'b')
axs[2].set(xlabel = 'Sample Points', ylabel = 'Error') #Sets ylabel with automatic rotation
plt.setp(axs[2].get_xticklabels(), rotation = 90) #Turns ticks 90 degrees
#======Plot End
#==========================Main Program End================================