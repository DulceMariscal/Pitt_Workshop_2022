# Programs 18c: Statistical Analysis on Microbes.png.
# See Figures 18.3 and 18.4.

import matplotlib.pyplot as plt
from skimage import io
import numpy as np
from skimage.measure import regionprops
from scipy import ndimage
from skimage import feature
from skimage.color import rgb2gray

Microbes=io.imread("Microbes.png")
fig1 = plt.figure()
plt.imshow(Microbes,cmap='gray',interpolation='nearest')
width, height, _ = Microbes.shape
Binary = np.zeros((width, height))

for i, row in enumerate(Microbes):
    for j, pixel in enumerate(row):
        if pixel[0] > 80:
            Binary[i, j] = 1

fig2 = plt.figure()                 
plt.imshow(Binary,cmap='gray')
#print('There are',int(np.sum(Binary)),'white pixels.')
print('There are {:,} white pixels'.format(int(np.sum(Binary))))

blobs = np.where(Binary>0.5, 1, 0)
labels, no_objects = ndimage.label(blobs)
props = regionprops(blobs)
print('There are {:,} clusters of cells:'.format(no_objects))

fig3 = plt.figure()
edges=feature.canny(Binary,sigma=2,low_threshold=0.5)
plt.imshow(edges,cmap=plt.cm.gray)

fig4 = plt.figure()
labeled_areas = np.bincount(labels.ravel())[1:]
print(labeled_areas)
plt.hist(labeled_areas,bins=no_objects)
plt.xlabel("Area",fontsize=15)
plt.ylabel("Number of clusters",fontsize=15)
plt.tick_params(labelsize=15)
plt.show()