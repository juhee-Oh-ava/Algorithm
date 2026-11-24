from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.
grid = [[0]*n for _ in range(n)]
# grid[r1-1][c1-1] = 1
# grid[r2-1][c2-1] = 1
visited = [[0]*n for _ in range(n)]
step = [[0]*n for _ in range(n)]

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
q = deque([])

def push(y, x, s):
    step[y][x] = s
    visited[y][x] = 1
    q.append((y, x))

def bfs(start):
    y, x = start
    q.append((y, x))
    visited[y][x] = 1

    while q:
        
        cy, cx = q.popleft()
        visited[cy][cx] = 1
        
        if cy == r2-1 and cx == c2-1:
            return 1
        
        for k in range(8):
            ny = cy + dy[k]
            nx = cx + dx[k]

            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == 0:
                    push(ny, nx, step[cy][cx] + 1)

if bfs((r1-1, c1-1)):
    print(step[r2-1][c2-1])
else:
    print(-1)


    

