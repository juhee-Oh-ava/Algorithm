N, M = map(int, input().split())
answer = []
flag = [0 for i in range(N+1)]
# Please write your code here.

def fun(curr_num, cnt):
    if curr_num == M+1:
        if print_answer():
            print(*answer)
        return
    

    for i in range(cnt, N+1):
        answer.append(i)
        flag[i] += 1
        fun(curr_num+1, i+1)
        flag[i] -= 1
        answer.pop()

def print_answer():

    for e in flag:
        if e >= 2:
            return 0
    return 1
    

fun(1, 1)
    