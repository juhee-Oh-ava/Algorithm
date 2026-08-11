def solution(n):
    ans = 0
    count = 0
    
    while(n > 10):
        if n % 2 == 1:
            count += 1
            n = n-1
        else:
            n = n // 2
            
    if n == 1:
        count += 1
    elif n == 2:
        count += 1
    elif n == 3:
        count += 2
    elif n == 4:
        count += 1
    elif n == 5:
        count += 2
    elif n == 6:
        count += 2
    elif n == 7:
        count += 3
    elif n == 8:
        count += 1
    elif n == 9:
        count += 2
    else: 
        count += 2
    
    return count