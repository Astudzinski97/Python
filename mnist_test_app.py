import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mnist_test.csv')
data = df.values
X = data[:, 1:]
Y = data[:, 0]

for i in range(10):
  Xi = X[Y == i]
  Mi = Xi.mean(axis=0)
  im = Mi.reshape(28,28)
  plt.imshow(im, cmap='gray')
  plt.title("Number: %s" % i)
  plt.show()