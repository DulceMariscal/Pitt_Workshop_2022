# Program 11b: Small-amplitude limit cycles.
# A cubic Lienard system. See Figure 10.1 and Table 11.1.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

a1, a2, a3, b2, b3 = 0.01, 1, 1/3, 1, 2  
xmin, xmax, ymin, ymax = -1, 1, -0.6, 1.4
# The Lienard system
def Lienard(x, t):
    # Here x[0] = x and x[1] = y    
    return np.array([ x[1]-a1*x[0]-a2*x[0]**2-a3*x[0]**3, \
                     -x[0]-a1*x[1]-b2*x[0]**2-b3*x[0]**3 ])

t = np.linspace(0, 200, 1000)

# Trajectories in forward time move away from inner limit cycle. 
xs=odeint(Lienard,[0.25,0],np.linspace(0,20,5000)) 
plt.plot(xs[:,0],xs[:,1], "r-")

# Unstable limit cycle. 
xs=odeint(Lienard,[0.295,0],np.linspace(0,50,5000)) 
plt.plot(xs[:,0],xs[:,1], 'b-', linewidth=2)

# Trajectories in forward time move away from inner limit cycle. 
xs=odeint(Lienard,[0.32,0],np.linspace(0,20,5000)) 
plt.plot(xs[:,0],xs[:,1], 'r-')

# Trajectories in forward time move towards the outer limit cycle. 
xs=odeint(Lienard,[0.44,0],np.linspace(0,22,5000)) 
plt.plot(xs[:,0],xs[:,1], 'r-')

# Stable limit cycle. 
xs=odeint(Lienard,[0.519,0],np.linspace(0,50,5000)) 
plt.plot(xs[:,0],xs[:,1], 'b-', linewidth=2)

# Trajectories in forward time move towards the outer limit cycle.   
xs=odeint(Lienard,[0.6,0],np.linspace(0,22,5000)) 
plt.plot(xs[:,0],xs[:,1], 'r-')

# Label the axes and set fontsizes. 
plt.xlabel("x",fontsize=15) 
plt.ylabel("y",fontsize=15) 
plt.tick_params(labelsize=15) 
plt.xlim(xmin,xmax) 
plt.ylim(ymin,ymax); 
plt.show()