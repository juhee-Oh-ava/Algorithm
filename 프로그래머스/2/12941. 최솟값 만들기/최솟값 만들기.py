import heapq

def solution(A,B):
    answer = 0
    
    heapq.heapify(A)  # A 자체가 최소 힙
    heapB = []
    
    for i in B:
        heapq.heappush(heapB, -i) # heap[0]에는 항상 가장 작은 값이 있다. 
        
    
    while heapB and A:
        min_a = heapq.heappop(A) 
        max_b = -heapq.heappop(heapB)

        answer += min_a * max_b


    return answer