def solution(s):
    
    int_lst = list(map(int, s.split()))
    
    mmax = max(int_lst)
    mmin = min(int_lst)
    
    answer = str(mmin) + ' ' + str(mmax)
    return answer