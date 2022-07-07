# Programs 16c: Bifurcation diagram of the Ikeda map.
# See Figure 16.16(d).
from matplotlib import pyplot as plt
import numpy as np
# Parameters
C=0.345913;kappa=0.0225;PMax=120;phi=np.pi;
halfN=1999;N=2*halfN+1;N1=1+halfN;
Esqr_up=[];Esqr_down=[];E1=0;E2=0;
ns_up=np.arange(halfN)  
ns_down=np.arange(N1,N)     

# Ramp the power up.
for n in ns_up:
    E2=E1*np.exp(1j*((abs(C*E1))**2-phi))
    E1=1j*np.sqrt(1-kappa)*np.sqrt(n*PMax/N1)+np.sqrt(kappa)*E2
    Esqr1=abs(E1)**2
    Esqr_up.append([n,Esqr1])

Esqr_up=np.array(Esqr_up)                        

# Ramp the power down.
for n in ns_down:
    E2=E1*np.exp(1j*((abs(C*E1))**2-phi))
    E1=1j*np.sqrt(1-kappa)*np.sqrt(2*PMax-n*PMax/N1)+np.sqrt(kappa)*E2
    Esqr1=abs(E1)**2
    Esqr_down.append([N-n,Esqr1])

Esqr_down=np.array(Esqr_down)

fig, ax = plt.subplots()
xtick_labels = np.linspace(0, PMax, 6)
ax.set_xticks([x/PMax*N1 for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])

plt.plot(Esqr_up[:,0],Esqr_up[:,1],'r.',markersize=0.1)
plt.plot(Esqr_down[:,0],Esqr_down[:,1],'b.',markersize=0.1)
plt.xlabel("Input",fontsize=15)
plt.ylabel("Output",fontsize=15)
plt.tick_params(labelsize=15)
plt.show()


