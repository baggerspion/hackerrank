import sys

def floyd_warshall():
    global matrix, N
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    
N, M = map(int, raw_input().split())

# Build and populate the matrix
matrix = [[sys.maxint for x in range(N)] for x in range(N)]
for x in range(N): matrix[x][x] = 0
for input in range(M):
    x, y, z = map(int, raw_input().split())
    matrix[x - 1][y - 1] = z
    
# Calculate all the shortest paths
floyd_warshall()

# Now check all input
for input in range(int(raw_input())):
    x, y = map(int, raw_input().split())
    if matrix[x - 1][y - 1] == sys.maxint:
        print "-1"
    else:
        print matrix[x - 1][y - 1]
