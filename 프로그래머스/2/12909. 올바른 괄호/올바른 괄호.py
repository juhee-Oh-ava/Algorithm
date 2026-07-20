def solution(s):
    # answer = True
    stack = []
    
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()
        
    
    if len(stack) == 0:
        return True
    else:
        return False
            
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print('Hello Python')

    # return True

