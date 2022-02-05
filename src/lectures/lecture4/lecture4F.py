# Program to multiply two matrices 
# using nested loops
# 3x3 matrix
A = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
B = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(str((matrix[i][j]))+"\t", end='')
        print("\n")
def matrix_x_matrix(X, Y):
    # iterate through rows of X
    # result is 3x4
    result = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
    for i in range(len(X)):
    # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result