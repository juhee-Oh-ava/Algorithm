def solution(brown, yellow):
    answer = []
    y = []
    count = brown + yellow
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yell = yellow // i
            if 2*(yell + i) + 4 == brown:
                y.append(yell+2)
                y.append(i+2)
            
    answer.append(y[0])
    answer.append(y[1])

    return answer