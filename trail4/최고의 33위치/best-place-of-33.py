def fun(i, j):
    dx = [-1, -1, 0, 0, 1, 1, 0, 1, -1]
    dy = [-1, 0, 1, -1, 0, 1, 0, -1, 1]

    x, y = i, j
    cnt = 0

    for k in range(9):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 1:
                cnt += 1

        # if nx < 0 or nx >= N or ny < 0 or ny >= N:
        #     continue
        # if arr[nx][ny] == 1:
        #     cnt += 1
    return cnt

    
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
lst = []
ss = 0

for i in range(N):
    for j in range(N):
        ss = fun(i, j)
        lst.append(ss)
print(max(lst))
