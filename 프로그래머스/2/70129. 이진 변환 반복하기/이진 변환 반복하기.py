def solution(s):
    answer = []
    zero_count = 0
    transform_count = 0
    
    while s!= "1":
        
        # 0의 개수 
        zero_count += s.count("0")
        
        # 1의 개수 추출
        one_count = s.count("1")
        
        # one_count (6)을 2진법으로.. 
        s = bin(one_count)[2:]
        
        transform_count += 1
    
    answer.append(transform_count)
    answer.append(zero_count)
        
    return answer