n, m = map(int, input().split())
A = list(map(int, input().split()))
answer = []
flag = [0 for i in range(n+1)]
result = []
# Please write your code here.

def fun(curr_num, cnt):
    if curr_num == m+1:
        if print_answer():
            return

    for i in range(cnt, len(A)):
        answer.append(A[i])
        flag[i+1] += 1
        fun(curr_num+1, i+1)
        flag[i+1] -= 1
        answer.pop()

def print_answer():
    ans = 0

    for ele in answer:
        ans = ans ^ ele
    
    result.append(ans)
    return result

        
fun(1, 0)
print(max(result))

