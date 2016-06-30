import matplotlib as m
m.use('TkAgg')
import matplotlib.pyplot as plt
#import quandl
from matplotlib import style
x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='skitscat', color='k', marker='*', s=100)

plt.xlabel('x')
plt.ylabel('y')

plt.title('Scatter')
plt.legend()
plt.show()
