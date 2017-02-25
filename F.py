N = int(input())

matrix = []

for i in range(N):
    matrix.append([int(x) for x in input().split()])

ribs = []

for i in range(N):
    k = 0
    for j in range(N):
        if matrix[i][j] != 0 :
            ribs.append([i,j,matrix[i][j]])

for elem in ribs:
    print(*elem)