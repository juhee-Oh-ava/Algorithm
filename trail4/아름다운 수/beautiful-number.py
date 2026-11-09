n = int(input())
answer = []
count = 0
# Please write your code here.
def beauty(lst):
    cnt = 1

    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            cnt += 1
        else:
            # 숫자가 바뀌면 지금까지 센 묶음을 검사
            if cnt % lst[i] != 0:
                return 0

            cnt = 1

    # 마지막 묶음은 반복문이 끝난 뒤 검사
    if cnt % lst[-1] != 0:
        return 0

    return 1
        

def fun(curr_num):
    global count 

    if curr_num == n + 1:
        if beauty(answer):
            count += 1
        return

    for i in range(1, 5):
        answer.append(i)
        fun(curr_num + 1)
        answer.pop()

fun(1)
print(count)