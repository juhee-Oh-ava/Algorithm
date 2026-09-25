n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
temp1 = []
temp2 = []

# [1, 2, 3, 1, 1, 5]

for i in range(len(blocks)):
    if i+1 < s1 or i+1 > e1:
        temp1.append(blocks[i])

# print(temp1)

for i in range(len(temp1)):
    if i+1 < s2 or i+1 > e2:
        temp2.append(temp1[i])

print(len(temp2))

for i in range(len(temp2)):
    print(temp2[i])


