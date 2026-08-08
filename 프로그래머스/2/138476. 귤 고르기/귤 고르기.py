from collections import Counter

def solution(k, tangerine):
    counts = Counter(tangerine)
    arr = sorted(counts.values(), reverse=True)

    total = 0

    for i in range(len(arr)):
        total += arr[i]

        if total >= k:
            return i + 1