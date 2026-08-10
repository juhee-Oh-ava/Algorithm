def solution(people, limit):
    answer = 0
    count = 0
    people.sort(reverse=True)
    # print(people)
    
    heavy = 0
    light = len(people)-1
    
    while heavy <= light:
        if people[heavy] + people[light] <= limit:
            light -= 1
        
        heavy += 1
        count += 1

    return count