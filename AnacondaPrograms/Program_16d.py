# Program 16d: Animation of the Ikeda Chaotic Attractor.

from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np

fig=plt.figure() 
plt.title('Animation Ikeda Chaotic Attractor')
plt.axis([0, 14, -2, 2])

B = 0.15
def ikeda(X):
    x, y = X
    xn = A + B*x*np.cos(x**2 + y**2) - B*y*np.sin(x**2 + y**2)
    yn = B*x*np.sin(x**2 + y**2) + B*y*np.cos(x**2 + y**2)
    return (xn, yn)

myimages = []
for A in np.arange(2, 10, 0.1):
    X0 = [A, 0]
    X, Y = [], []

    for i in range(5000):
        xn, yn = ikeda(X0)
        X, Y = X + [xn], Y + [yn]
        X0 = [xn, yn]         
    myimages.append(plt.plot(X, Y, 'b.', markersize=0.2))     

my_anim = ArtistAnimation(fig, myimages, blit=False, interval=100)
plt.show()