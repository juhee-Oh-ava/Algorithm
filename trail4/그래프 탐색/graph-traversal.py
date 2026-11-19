n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
visited = [0 for i in range(n+1)]
# Please write your code here.
cnt = 0

graph = [[] for _ in range(n+1)]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)


def dfs(start):
    global cnt 
    visited[start] = 1
    for curr_v in graph[start]:
        if visited[curr_v] == 1:
            continue
        cnt += 1
        dfs(curr_v)
        visited[curr_v] == 0
        
dfs(1)
print(cnt)