import numpy as np
import matplotlib.pyplot as plt

#n is the number of recursive calls
#p are the coordinates of eache vertice
#w is the distance between each plot
def draw_squares(ax,n,p,w):
    
    #copying the arrays to each of the four squares
    UpLeft = np.copy(p)  
    UpRight = np.copy(p)
    DownLeft = np.copy(p)
    DownRight = np.copy(p)
        
    if n > 0:   
        
        #Moves vertices in different ways to create upper-right square 
        UpRight[0] = UpRight[0] + w*.75
        UpRight[1][0] = UpRight[1][0] + w*.75
        UpRight[1][1] = UpRight[1][1] + w*.25
        UpRight[2] = UpRight[2] + w*.25
        UpRight[3][0] = UpRight[3][0] + w*.25
        UpRight[3][1] = UpRight[3][1] + w*.75
        UpRight[4] = UpRight[4] + w*.75
        
        #Moves vertices in different ways to create bottom-right square 
        DownRight[0][0] = DownRight[0][0] + w*.75 
        DownRight[0][1] = DownRight[0][1] - w*.25 
        DownRight[1][0] = DownRight[1][0] + w*.75
        DownRight[1][1] = DownRight[1][1] - w*.75
        DownRight[2][0] = DownRight[2][0] + w*.25
        DownRight[2][1] = DownRight[2][1] - w*.75
        DownRight[3][0] = DownRight[3][0] + w*.25
        DownRight[3][1] = DownRight[3][1] - w*.25
        DownRight[4][0] = DownRight[4][0] + w*.75
        DownRight[4][1] = DownRight[4][1] - w*.25       
        
        #Moves vertices in different ways to create bottom-left square 
        DownLeft[0] = DownLeft[0] - w*.25
        DownLeft[1][0] = DownLeft[1][0] - w*.25
        DownLeft[1][1] = DownLeft[1][1] - w*.75
        DownLeft[2] = DownLeft[2] - w*.75
        DownLeft[3][0] = DownLeft[3][0] - w*.75
        DownLeft[3][1] = DownLeft[3][1] - w*.25
        DownLeft[4] = DownLeft[4] - w*.25
        
        #Moves vertices in different ways to create upper-left square  
        UpLeft[0][0] = UpLeft[0][0] - w*.25
        UpLeft[0][1] = UpLeft[0][1] + w*.75
        UpLeft[1][0] = UpLeft[1][0] - w*.25
        UpLeft[1][1] = UpLeft[1][1] + w*.25
        UpLeft[2][0] = UpLeft[2][0] - w*.75
        UpLeft[2][1] = UpLeft[2][1] + w*.25
        UpLeft[3][0] = UpLeft[3][0] - w*.75
        UpLeft[3][1] = UpLeft[3][1] + w*.75
        UpLeft[4][0] = UpLeft[4][0] - w*.25
        UpLeft[4][1] = UpLeft[4][1] + w*.75
        
        #Recursive call for upper-right square. 
        ax.plot(UpRight[:,0],UpRight[:,1],color='k')
        draw_squares(ax,n-1,UpRight,w/2)
        
        #Recursive call for bottom-right square
        ax.plot(DownRight[:,0],DownRight[:,1],color='k')
        draw_squares(ax,n-1,DownRight,w/2)
        
        #Recursive call for bottom-left square.
        ax.plot(DownLeft[:,0],DownLeft[:,1],color='k')
        draw_squares(ax,n-1,DownLeft,w/2)
        
        #Recursive call for upper-left square.
        ax.plot(UpLeft[:,0],UpLeft[:,1],color='k')
        draw_squares(ax,n-1,UpLeft,w/2)
        
plt.close("all") 
orig_size = 1000
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
ax.plot(p[:,0],p[:,1],color='k')
draw_squares(ax,3,p,orig_size) #we take the original size since in this case it means the length of the square
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')