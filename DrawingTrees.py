import numpy as np
import matplotlib.pyplot as plt

# n is the number of calls to the method
# p are the coordinates where the points are located
# xAxis is the quantity that the original point moves to the right and to the left
# yAxis is the quantity that makes the original point moving down 
# w is the width. it help us to reduce values

def Drawing_Lines(ax, n, p, xAxis, yAxis, w):
    if n>0:

        RightLine = np.copy(p)
        LeftLine = np.copy(p)
        
        #this moves the the point xAxis to the right and yAxis down
        RightLine = [p[0] + xAxis, p[1] - yAxis]  
        #this moves the the point xAxis to the left and yAxis down
        LeftLine = [p[0] - xAxis, p[1] - yAxis]
        
        # creates the lines
        ax.plot([p[0], RightLine[0]], [p[1], RightLine[1]],[p[0], LeftLine[0]], [p[1], LeftLine[1]], color = 'k')
        # this recursive call reduces the right line by xAxis/2 but have the same length in yAxis
        Drawing_Lines(ax, n-1, RightLine, xAxis*w, yAxis, w)
        # this recursive call reduces the left line by xAxis/2 but have the same length in yAxis
        Drawing_Lines(ax, n-1, LeftLine, xAxis*w, yAxis, w)

plt.close("all")

p = np.array([0,0])
fig, ax = plt.subplots()
Drawing_Lines(ax, 4, p, 1000, 1000, .5)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('trees.png')

        
        