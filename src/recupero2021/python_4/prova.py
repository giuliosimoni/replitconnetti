import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd


input = np.loadtxt("ex2_data_python_4.txt", dtype='i')
print(input)

dataset = pd.read_csv('points.csv')
X = dataset.iloc[:,0:1].values
Y = dataset.iloc[:,1:2].values

coordinatesCenter = []

def findCenter(xList, yList, coordinates):
  xCenter=np.sum(xList)/len(xList)
  yCenter=np.sum(yList)/len(yList)
  coordinates.append(xCenter)
  coordinates.append(yCenter)
  return coordinates


findCenter(X,Y, coordinatesCenter)

np.array(coordinatesCenter)

plt.scatter(X, Y, label= 'Point (X;Y)', color='k')
plt.scatter(coordinatesCenter[0], coordinatesCenter[1], label= 'Center (X;Y)', color='k')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Centroid coordinates')
plt.legend()
plt.show()