import numpy as np

data = np.loadtxt("src/ex2_data_python_4.txt", dtype='f') # 'f'='float'

X=[]
Y=[]
for i in range(len(data)):
  for j in range(2):
    if j==0:
      X.append(data[i][j])
    else:
      Y.append(data[i][j])

print(X)
print(Y)

coordinatesCenter = []

def findCenter(xList, yList, coordinates):
  xCenter=np.sum(xList)/len(xList)
  yCenter=np.sum(yList)/len(yList)
  coordinates.append(xCenter)
  coordinates.append(yCenter)
  return coordinates


findCenter(X,Y, coordinatesCenter)

np.array(coordinatesCenter)

print(coordinatesCenter)
