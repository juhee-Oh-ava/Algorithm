from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
step = [[0]*m for _ in range(n)]
# Please write your code here.
q = deque([])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def push(y, x, s):
    step[y][x] = s
    visited[y][x] = 1
    q.append((y, x))


def bfs(start):
    global count
    y, x = start
    visited[y][x] = 1
    q.append((y, x))

    while q:
        cy, cx = q.popleft()
        visited[cy][cx] = 1

        if cy == n-1 and cx == m-1:
            return 1

        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]

            if 0 <= nx < m and 0 <= ny < n:
                if a[ny][nx] != 0 and visited[ny][nx] == 0:
                    push(ny, nx, step[cy][cx] + 1)
        

# push(0, 0, 0)
if bfs((0,0)) == 1:
    print(step[n-1][m-1])
else:
    print(-1)
