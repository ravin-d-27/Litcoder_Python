def nth_smallest_element(arr, n):
    return sorted(arr)[n-1]

def beauty_of_subarrays(arr, k, n):
    
    answer = []
    scope = arr[:k]
    for i in range(len(arr)-k+1):
        n_small = nth_smallest_element(scope, n)
        answer.append(n_small)
        
        if len(arr)>i+k:
            scope.remove(arr[i])
            scope.append(arr[i+k])

    return answer


arr = list(map(int, input().strip().split()))
k = int(input())
n = int(input())

print(beauty_of_subarrays(arr,k,n))