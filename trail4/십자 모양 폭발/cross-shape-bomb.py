def bomb(r, c, k):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    x, y = c-1, r-1

    grid[y][x] = 0

    for i in range(4):
        for j in range(1, k):
            nx = x + dx[i]*j
            ny = y + dy[i]*j

            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            grid[ny][nx] = 0

def gravity():
    result = [[0]*n for _ in range(n)]

    for col in range(n):
        write_row = n-1

        for row in range(n-1, -1, -1):
            if grid[row][col] != 0:
                result[write_row][col] = grid[row][col]
                write_row -= 1
    return result
    
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
result = []
# Please write your code here.

bomb(r, c, grid[r-1][c-1])
result = gravity()

for r in result:
    print(*r)

