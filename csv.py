import matplotlib as m
m.use('TkAgg')
import matplotlib.pyplot as plt
#import quandl
from matplotlib import style
import numpy as np

'''
#Part 1
import csv

x = []
y = []

with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
'''


x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)



plt.plot(x,y, label='CSV')
plt.xlabel('x')
plt.ylabel('y')
plt.title('CSV')
plt.legend()
plt.show()
