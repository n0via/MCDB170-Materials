# This script does not run in JupyterLab.
# Download and install the Thonny editor from "Thonny.org".
# Install "numpy" and "matplotlib" in the "Tools->Manage packages..." menu.
# Then run this script in the Thonny editor.

import numpy as np
import matplotlib.pyplot as plt
import time


# Define a function to calcualte the number of alive neighbor cells


# 1. Initialize a matrix with random 0's and 1's.
world_current = np.random.randint(0, 2, (100, 100))
world_future = np.zeros(world_current.shape)


# Image plotting code
plt.figure(1, figsize=(6,5))
plt.ion()
plt.show()
im = plt.imshow(world_current)
plt.draw()
plt.pause(1)



# 2. Write a for-loop with some iterations.

for c in range(10000):
    a = world_current
    tmp = np.roll(a, 1, axis=0) + np.roll(a, -1, axis=0) + np.roll(a, 1, axis=1) + np.roll(a, -1, axis=1) \
          + np.roll(a, (1,1), axis=(0,1)) + np.roll(a, (1,-1), axis=(0,1)) \
          + np.roll(a, (-1,1), axis=(0,1)) + np.roll(a, (-1,-1), axis=(0,1))
    
    #cond1 = np.logical_and(world_current == 1, np.logical_or (tmp == 2 , tmp ==3))
    cond1 = (world_current == 1) & ((tmp == 2) | (tmp ==3))
    cond2 = (world_current == 0) & (tmp == 3)
    world_future *= 0
    world_future[cond1] = 1
    world_future[cond2] = 1
    

    world_current, world_future = world_future, world_current # Swaps the variable name of two arrays
    print(c)
    
    
    # To speed up, only the image data is updated, instead of using 'imshow' everytime.
    im.set_data(world_current)
    plt.draw()
    plt.pause(0.01)
    






