#esercizi 3 parte 2
import sys
import numpy as np

#OPERAZIONI CON MATRICI

#moltiplicazione matrice per scalare
a=3
b=[[3,6,9], [1,2,3], [2,4,8]]
def matrix_per_scalar(matrix, scalar):
  result=[]
  for i in range(len(matrix)):
    tmp=[]
    for j in range(len(matrix[i])):
      tmp.append(matrix[i][j]*scalar)
    result.append(tmp)
  return result

def print_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      print(str((matrix[i][j]))+"\t", end='')
    print("\n")

print("Risultato matrice x scalare:")
print_matrix(matrix_per_scalar(b,a))

#moltiplicazioni con matrici usando liste annidate

X = [[12,7,3],[4,5,6],[7,8,9]]
Y = [[5,8,1,2], [6,7,3,0], [4,5,9,1]]
result = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
  # iterate through columns of Y
  for j in range(len(Y[0])):
    # iterate through rows of Y
    for k in range(len(Y)):
      result[i][j] += X[i][k] * Y[k][j]

# Program to multiply two matrices using list comprehension
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

#modo più smart per liste annidate
def matrix_x_matrix(X,Y): #attenzione alle dimensioni delle matrici di input
  result = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
  for i in range(len(X)):
  # iterate through columns of Y
    for j in range(len(Y[0])):
  # iterate through rows of Y
      for k in range(len(Y)):
        result[i][j] += X[i][k] * Y[k][j]
  return result

print("Risultato matrice x matrice:")
print_matrix(matrix_x_matrix(X,Y))