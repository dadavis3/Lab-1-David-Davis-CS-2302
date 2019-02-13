import matplotlib.pyplot as plt
import numpy as np
import math 

#Method to draw a circle 
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

#method the modify circles
#n is the number of calls to the method
#center is the center of the circle
#radius is the radius of the circle
#w will help us to reduce the size of the circles 
def draw_circles(ax,n,center,radius,w):
    if n>0:
       
        x,y = circle(center,radius)
        
        #In this recursive call we just reduce the size of the radius that way 
        #the circles get smaller each call
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,[radius*w,0],radius*w,w) 
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 8, [100,0], 100,0.6)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')