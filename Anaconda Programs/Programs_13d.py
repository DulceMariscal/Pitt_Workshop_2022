# Program 13d: The Leslie matrix population plot. See Example 4.
# Compute the population distribution after 50 years.

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

t_span = 51
L=np.array([[0,3,1],[0.3,0,0],[0,0.5,0]])

X=[0]*t_span;X1=[0]*t_span;X2=[0]*t_span;X3=[0]*t_span;
X[0]=np.array([[1000],[2000],[3000]])

for i in range(t_span):
     X[i] =np.array(np.dot(LA.matrix_power(L,i),X[0])).tolist()
     X1[i] = X[i][0]
     X2[i] = X[i][1]
     X3[i] = X[i][2]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(X1,color='r',label='Age Class 1')
ax.plot(X2,color='b',label='Age Class 2')
ax.plot(X3,color='k',label='Age Class 3')
plt.xlabel("Age classes",fontsize=15) 
plt.ylabel("Populations",fontsize=15) 
plt.tick_params(labelsize=15)
legend = plt.legend(loc='upper center',shadow=True)
plt.show()