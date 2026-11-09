K, N = map(int, input().split())
answer = []

def choose(curr_num):
    if curr_num == N + 1:
        print(*answer)
        return

    for i in range(1, K + 1):
        answer.append(i)      # 이번 자리에 i를 넣고
        choose(curr_num + 1)  # 다음 자리를 끝까지 탐색한 뒤
        answer.pop()          # 이번 자리를 비워 다음 i를 시도

choose(1)