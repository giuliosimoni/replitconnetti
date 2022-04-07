A=[2,4,3]
B=[6,5,1]

def dot_product(X,Y):
  dotProduct=0
  for i in range(len(X)):
    value=X[i]*Y[i]
    dotProduct+=value
  return dotProduct


d_p2=dot_product(A,B)

import numpy as np

d_p1=np.dot(A,B)

print(d_p1, d_p2)



import numpy as np

A = [[12,7,3], [4 ,5,6], [7 ,8,9]]

B = [[5,8,1,2], [6,7,3,0], [4,5,9,1]]

def matrix_mult(X,Y):
  result = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
  for i in range(len(X)):
    for j in range(len(Y[0])):
      for k in range(len(Y)):
        result[i][j] += X[i][k] * Y[k][j]
  return result

C=matrix_mult(A,B)
print(C)
print()

A=np.array(A)
B=np.array(B)
print(A.dot(B))
