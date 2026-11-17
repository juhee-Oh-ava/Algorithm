n = int(input())
answer = []
visited = [0 for i in range(n)]
# Please write your code here.

def fun(curr_num):
    if curr_num == n+1:
        print_answer()
        return
    
    for i in range(1, n+1):
        if visited[i-1] == 1:
            continue
        answer.append(i)
        visited[i-1] += 1 
        fun(curr_num+1)
        answer.pop()
        visited[i-1] -= 1

def print_answer():
    
    for v in visited:
        if v == 1:
            continue
        else:
            return 0
    print(*answer)
    return 1

fun(1)
