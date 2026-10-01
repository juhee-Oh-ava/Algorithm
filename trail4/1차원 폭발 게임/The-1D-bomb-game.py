def bomb(n,m):
    cnt = 1
    exploded = False

    for i in range(n):
        if i < n-1 and numbers[i] == numbers[i+1]:
            cnt += 1
        else:
            if cnt >= m:
                for i in range(i, i-cnt, -1):
                    numbers[i] = 0
                exploded = True
            cnt = 1
    return exploded
        
n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.


while(True):
    
    result = bomb(len(numbers), m)
    
    if not result:
        break
    
    temp = []
    for i in range(len(numbers)):
        if numbers[i] != 0:
            temp.append(numbers[i])
    numbers = temp
        
print(len(numbers))
for row in numbers:
    print(row)
    



                
        
        
            

    