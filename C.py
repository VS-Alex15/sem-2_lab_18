N = int(input())
M = int(input())
graph = [[] for i in range(N)]
for edge in range(M):
    a, b = [int(x) for x in input().split()]
    graph[a].append(b)

def dfs(vertex, graph, used=set()):
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)
k = 1
for i in range(N):
    used = set()
    dfs(i,graph,used)
    if len(used)!=N:
        k = 0
        break

if k == 1:
    print('YES')
else: print('NO')