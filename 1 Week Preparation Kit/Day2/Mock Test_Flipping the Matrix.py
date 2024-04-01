#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
def flippingMatrix(matrix):
    n = len(matrix) // 2
    max_sum = 0
    for i in range(n):
        for j in range(n):
            max_sum += max(matrix[i][j], matrix[2*n-i-1][j], matrix[i][2*n-j-1], matrix[2*n-i-1][2*n-j-1])
    return max_sum