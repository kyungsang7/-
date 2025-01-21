from collections import deque

N,M,V = map(int,input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(N+1):
    adj[i] = sorted(adj[i])

def DFS(num):
    global visited
    visited.append(num)
    for i in adj[num]:
        if not i in visited:
            DFS(i)

def BFS(num):
    global visited
    queue = deque([num])
    visited.append(num)
    while queue:
        num = queue.popleft()
        for i in adj[num]:
            if not i in visited:
                visited.append(i)
                queue.append(i)

visited = []
DFS(V)
print(*visited)
visited = []
BFS(V)
print(*visited)