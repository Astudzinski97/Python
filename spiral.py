# formula for spiral points x = rcos(a), y = rsin(a)

import numpy as np
import matplotlib.pyplot as plt

radius_max = 10
angle_max = np.pi

def make_spiral(rad_max, angl_max):
  radius = np.linspace(1,rad_max, 500)
  angles = np.empty((6,500))

  for i in range(6):
    start_angl = np.pi*i/3.0 #from 0 to angl_max/2, then pi/3 to pi/3+angl_max/2 etc.
    max_angl = start_angl+angl_max/2.0
    calc_angl = np.linspace(start_angl, max_angl, 500)
    angles[i] = calc_angl
  
  x = np.empty((6, 500))
  y = np.empty((6, 500))
  for i in range(6):
      x[i] = radius * np.cos(angles[i])
      y[i] = radius * np.sin(angles[i])

  X = np.empty((3000,2))
  X[:,0] = x.flatten() #convert to one-dimensional array
  X[:,1] = y.flatten()

  colors = np.array([0]*500 + [1]*500 + [0]*500 + [1]*500 + [0]*500 + [1]*500)
  X += np.random.randn(3000, 2)*0.15 # randomize to not make it too smooth
                       
  return X, colors

A, B = make_spiral(radius_max, angle_max)
plt.scatter(A[:,0],A[:,1],c=B)
plt.show();