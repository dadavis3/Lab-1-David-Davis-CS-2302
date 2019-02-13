#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 15:52:46 2019

@author: daviddavis
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

#this is the method to create the circle
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

#this method creates the 5 circles in each circle
#n is the total number of calls to the method
#center is the center of the middle circle which will be motified to create all circles
#radius is the radius of each circle
#w will help us tu reduce sizes
def draw_circles(ax,n,center,radius,w):
    
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
       
        #creates the middle circle and each time reduces the radius by w
        draw_circles(ax,n-1,center,radius*w,w) 
        #creates the right circle and keeps the same y coordinate
        draw_circles(ax,n-1,[center[0]+radius*2*w,center[1]],radius*w,w)
        #creates the left circle and keeps the same y coordinate
        draw_circles(ax,n-1,[center[0]-radius*2*w,center[1]],radius*w,w)
        #creates the top circle and keeps the same x coordinate
        draw_circles(ax,n-1,[center[0],center[1]+radius*2*w],radius*w,w)
        #creates the bottom circle and keeps the same x coordinate
        draw_circles(ax,n-1,[center[0],center[1]-radius*2*w],radius*w,w)
        
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 3, [0,0], 100,.33)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')

        