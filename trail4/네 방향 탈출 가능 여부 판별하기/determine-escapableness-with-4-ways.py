n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0]*m for _ in range(n)]
q = []

def bfs(start):

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    y,x = start
    visited[y][x] = 1
    q.append((y, x))

    while q:

        cy, cx = q.pop()

        if cy == n-1 and cx == m-1:
            return 1

        if a[cy][cx] != 1:
            return 0
        
        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]

            if 0 <= nx < m and 0 <= ny < n:
                if visited[ny][nx] == 0 and a[ny][nx] == 1:
                    visited[ny][nx] = 1
                    q.append((ny, nx))

    return 0    
        
    
print(bfs((0, 0)))