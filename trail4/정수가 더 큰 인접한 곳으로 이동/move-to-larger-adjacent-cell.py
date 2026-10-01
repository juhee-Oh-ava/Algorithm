def finding(i, j):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    temp.append(a[i][j])
    cr, cc = i, j

    while(True):
        flag = False

        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]

            if nr < 1 or nr > n or nc < 1 or nc > n:
                continue

            if a[cr][cc] < a[nr][nc]:
                temp.append(a[nr][nc])
                cr = nr
                cc = nc
                flag = True
                break
                    
        if not flag:
            return temp
        

            


n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
temp = []
result = []


result = finding(r, c)
for k in result:
    print(k, end=" ")
            