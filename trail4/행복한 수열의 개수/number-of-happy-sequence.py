n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# Please write your code here.

if n ==1 and m == 1:
    ans = 2

for r in grid:
    cnt = 1
    f = False
    for i in range(len(r)-1):
        if r[i] == r[i+1]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            f = True
        if f:
            ans += 1
            break



for i in range(len(grid)):
    cnt = 1
    f = False
    for j in range(len(grid)-1):
        if grid[j][i] ==  grid[j+1][i]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            f = True
        if f:
            ans += 1
            break
        
print(ans)


