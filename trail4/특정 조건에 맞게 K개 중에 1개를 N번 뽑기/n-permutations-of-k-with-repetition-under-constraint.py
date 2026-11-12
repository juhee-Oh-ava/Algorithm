K, N = map(int, input().split())
answer = []
# Please write your code here.

def fun(cur_num):
    if cur_num == N+1:
        print_answer()
        if print_answer():
            print(*answer)
        return
    
    for i in range(1, K+1):
        answer.append(i)
        fun(cur_num+1)
        answer.pop()

def print_answer():
    cnt = 1
    for i in range(len(answer)-1):
        if answer[i] == answer[i+1]:
            cnt += 1
            if cnt >= 3:
                return 0
        else:
            cnt = 1
    return 1



                
fun(1)
