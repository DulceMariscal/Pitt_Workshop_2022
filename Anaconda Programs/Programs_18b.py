# Programs_18b: Color picture of a raccoon.
# See Figure 18.2.

from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
face = misc.face()

fig1 = plt.figure()
plt.imshow(face)
width, height, _ = face.shape

face[100, 100]                      # RGB values and data type.
print('RGB value=',face[100, 100])  # RGB values of pixel.
print('Image dimensions: {}x{}'.format(width, height))
WhitePixels = np.zeros((width, height))
                    
def white_pixel(pixel, threshold):
    return 1 if all(value > threshold for value in pixel) else 0
for i, row in enumerate(face):
    for j, pixel in enumerate(row):
        WhitePixels[i, j] = white_pixel(pixel, threshold=180)                              
fig2 = plt.figure()
plt.imshow(WhitePixels,cmap='gray')
print('There are {:,} white pixels'.format(int(np.sum(WhitePixels))))
plt.show()

