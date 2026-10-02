def finding(r, c):
    
    # sliced의 i-1 행의 모든 열들을 1로 바꿔라
    for i in range(len(sliced)):
        for j in range(len(sliced[i])):
            if i == r-1:
                sliced[i][j] = 1
    
    return sliced

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 블록의 크기는 항상 1 x M 이잖아.
# k 열부터 k+m-1 열까지만 보면 됨
# grid 를 k 부터 k+m-1 까지로 어떻게 자르지.. 슬라이싱으로?

sliced = [row[k-1:k+m-1] for row in grid]
found = False



for i in range(len(sliced)):
    for j in range(len(sliced[i])):
        if sliced[i][j] == 1:
            sliced = finding(i, j)
            found = True
            break
    if found:
        break

if not found:
    for j in range(len(sliced[-1])):
        sliced[-1][j] = 1



for i in range(len(grid)):
    grid[i][k-1:k+m-1] = sliced[i]


for row in grid:
    print(*row)