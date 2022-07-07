# Programs 10f: Homoclinic Bifurcation. See Figure 10.2.
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.integrate import odeint

fig=plt.figure()
plt.axis([-1.5, 1.5, -1.5, 1.5])
myimages=[]
plt.title("Homoclinic Bifurcation")

def Homoclinic1(x, t):
    return [x[1]+10*x[0]*(0.1-x[1]**2), -x[0]+C]

time = np.arange(0, 200, 0.01)
x0=[1,0]
for C in np.arange(-0.2, 0.2, 0.01):
    xs = odeint(Homoclinic1, x0, time)
    imgplot = plt.plot(xs[:,0], xs[:,1], "r-")
    myimages.append(imgplot)
   
my_anim = animation.ArtistAnimation(fig,myimages,interval=100,blit=False,repeat_delay=100)
plt.show()