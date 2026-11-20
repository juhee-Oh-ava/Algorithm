n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
# Please write your code here.


def dfs(y, x):

    if grid[y][x] == 0:
        return False

    if x == m-1 and y == n-1:
        return True

    dx = [1, 0]
    dy = [0, 1]
    cx = x
    cy = y

    for k in range(2):
        nx = cx + dx[k]
        ny = cy + dy[k]

        if 0 <= nx and nx < m and 0 <= ny and ny < n:
            if visited[ny][nx] == 0 and grid[ny][nx] == 1:
                visited[ny][nx] = 1
                if dfs(ny, nx):
                    return True
    return False

print(1 if dfs(0, 0) else 0)
    

