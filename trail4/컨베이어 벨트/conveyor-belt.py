n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

d.reverse()

for _ in range(t):
    x, y = u[n-1], d[0]
    u[1:n] = u[0:n-1]
    u[0]= y
    d[:n-1] = d[1:n]
    d[n-1] = x

d.reverse()
print(*u)
print(*d)