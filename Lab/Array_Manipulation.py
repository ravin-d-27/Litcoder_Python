def manipulate(array_size, queries):
    array = [0 for i in range(array_size)]
    for query in queries:
        start_idx, end_idx, value = query
        array[start_idx - 1:end_idx] = [x + value for x in array[start_idx - 1:end_idx]]

    return max(array)

qs = []
array_size = int(input().strip())
query_count = int(input().strip())
for i in range(query_count):
    q = list(map(int, input().strip().split()))
    qs.append(q)
print(manipulate(array_size, qs))
