n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0]*n for _ in range(n)]
answer = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(y, x):
    visited[y][x] = 1
    count = 1

    cy = y
    cx = x

    for k in range(4):
        ny = cy + dy[k]
        nx = cx + dx[k]

        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if grid[ny][nx] == 1 and visited[ny][nx] == 0:
                count += dfs(ny, nx)
    return count 
                
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and visited[i][j] == 0:
            answer.append(dfs(i, j))

print(len(answer))
answer.sort()
for x in answer:
    print(x)
