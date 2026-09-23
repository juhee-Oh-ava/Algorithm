n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
# 124
# 593
# 651
d.reverse()

for _ in range(t):
    x, y, z = l[n-1], r[n-1], d[0]
    l[1:n] = l[0:n-1]
    l[0] = z
    r[1:n] = r[:n-1]
    r[0] = x
    d[:n-1] = d[1:n]
    d[n-1] = y

d.reverse()
print(*l)
print(*r)
print(*d) 

