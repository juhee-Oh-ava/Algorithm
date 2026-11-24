from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(start):
    y, x = start
    q = deque([(y, x)])
    visited = [[0] * n for _ in range(n)]
    visited[y][x] = 1

    while q:
        cy, cx = q.popleft()

        for d in range(4):
            ny = cy + dy[d]
            nx = cx + dx[d]

            if 0 <= ny < n and 0 <= nx < n:
                if grid[ny][nx] < grid[y][x] and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny, nx))

    return visited


def finding(visited, start):
    mmax = None

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1 and (i, j) != start:
                if mmax is None or grid[i][j] > mmax:
                    mmax = grid[i][j]

    return mmax


def location_y(t, visited):
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1 and grid[i][j] == t:
                return i


def location_x(t, s, visited):
    for j in range(n):
        if visited[s][j] == 1 and grid[s][j] == t:
            return j


for _ in range(k):
    visited = bfs((r, c))
    t = finding(visited, (r, c))

    if t is None:
        break

    s = location_y(t, visited)
    r, c = s, location_x(t, s, visited)

print(r + 1, c + 1)