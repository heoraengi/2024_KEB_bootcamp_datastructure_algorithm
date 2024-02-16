from collections import deque

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    visited = [0] * (n + 1)
    distance = [0] * (n + 1)
    answer = []
    q = deque([start])
    visited[start] = 1
    distance[start] = 0
    while q :
        now = q.popleft()
        for next in graph[now]:
            if visited[next] == 0 :
                visited[next] = 1
                q.append(next)
                distance[next] = distance[now] + 1
                if distance[next] == k:
                    answer.append(next)

    if len(answer) == 0:
        print(-1)
    else :
        answer.sort()
        for next in answer:
            print(next)

bfs(x)
