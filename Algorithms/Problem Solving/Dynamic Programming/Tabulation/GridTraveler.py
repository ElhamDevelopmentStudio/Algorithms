"""
Source: https://www.youtube.com/watch?v=oBt53YbR9Kk
Description: Given a grid of m x n find a way to get from the starting point (0, 0) to the end point. You can only more right or down other moves are not allowed.
"""
# def GridTraveler(x, y):
#   dimentions = {}
#   for i in range(x + 1):
#     for j in range(y + 1):
#       dimentions[(i, j)] = 0

#   dimentions[(1, 1)] = 1
#   for xDim, yDim in dimentions:
#     # x + 1 => 0, 0 = (0, 1), (1, 0)
#     if xDim + 1 <= x:
#         dimentions[(xDim + 1, yDim)] += dimentions[(xDim, yDim)]
#     if yDim + 1 <= y:
#         dimentions[(xDim, yDim + 1)] += dimentions[(xDim, yDim)]

#   return dimentions[(x, y)]

def grid_traveler(m, n):
    dimentions = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    dimentions[1][1] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                continue
            dimentions[i][j] = dimentions[i - 1][j] + dimentions[i][j - 1]
    
    return dimentions[m][n]


print(grid_traveler(3, 3))