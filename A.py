N = int(input())
M = int(input())
graph = [[] for i in range(N)]
for edge in range(M):
    a, b = [int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)

def dfs(vertex, graph, used = set()):
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)

k = 1

for i in range(N):
    if len(graph[i])%2==1:
        k = 0

components = 0

used = set()
for vertex in range(N):
    if vertex not in used:
        dfs(vertex, graph, used)
        components += 1

if components>1 :
    k=0


if k == 1:
    print('YES')
else:
    print('NO')