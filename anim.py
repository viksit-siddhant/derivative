import numpy as np
from  sympy import *
import matplotlib.pyplot as plt
from matplotlib import animation,style
import math

style.use('ggplot')
fig = plt.figure()

#x-range and y-range of the plot. Change it to whatever you want to
xlim = (-5,0)
ylim = (-5,20)

ax = plt.axes(xlim=xlim, ylim=ylim)
x = Symbol('x')

#Function you want to plot
f = (x + 1)*(x + 2)*(x + 3)*(x + 4)

#Change this to change the speed at which the line moves
delta_x = 0.025

np_f = utilities.lambdify(x,f,'numpy')
line, = ax.plot([], [], lw=2)
fx = np.linspace(xlim[0],xlim[1],256)
fy = np_f(fx)
func, = ax.plot(fx,fy)

df = utilities.lambdify(x,diff(f,x),'numpy')

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

def animate(i):
    di = df(i)
   #Normalize the length of the line
    offset = 0.5
    theta = math.atan2(di*2*offset/abs(ylim[0]-ylim[1]),offset*2/abs(xlim[0]-xlim[1]))
    offset *= math.cos(theta)

    print(offset,end='\r')
    x = np.linspace(i-offset,i+offset,2)
    b = np_f(i) - i*di
    y = x*di + b
    line.set_data(x, y)
    return line,

def gen_x():
    num = xlim[0]
    while num <= xlim[1]:
        num += delta_x
        yield num

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=gen_x, interval=16, blit=True)

plt.show()
