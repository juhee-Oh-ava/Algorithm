n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
visited = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = []

def bfs(start):
    count = 1
    i, j = start
    q.append((i, j))
    visited[i][j] = 1

    while q:

        cy, cx = q.pop()
        visited[cy][cx] = 1
        
        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[ny][nx] == 0 and grid[ny][nx] == 0:
                    visited[ny][nx] = 1
                    count += 1
                    q.append((ny, nx))
    return count

result = 0
for y, x in points:
    for r in range(n):
        for c in range(n):
            if r == y-1 and c == x-1:
                if visited[r][c] == 0 and grid[r][c] == 0:
                    result += bfs((r, c))

print(result)