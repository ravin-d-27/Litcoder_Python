def kth_smallest_trimmed_number(nums, queries):
    answer = []
    
    for query in queries:
        position, trim = query
        trimmed_nums = [int(num[-trim:]) for num in nums]
        sorted_indices = sorted(range(len(trimmed_nums)), key=lambda k: (trimmed_nums[k], k))
        original_indices = sorted(range(len(nums)), key=lambda k: sorted_indices[k])
        
        answer.append(original_indices.index(position))
    
    return answer

# Exercise-1
input_1 = "113 933 231 719"
queries_1 = [
    [1, 1],
    [2, 2],
    [4, 2],
    [1, 3]
]

nums_1 = input_1.split()
result_1 = kth_smallest_trimmed_number(nums_1, queries_1)
print("Exercise-1 Output:", " ".join(map(str, result_1)))

# Exercise-2
input_2 = "123 456 246 369"
queries_2 = [
    [1, 1],
    [2, 2],
    [4, 2],
    [1, 3]
]

nums_2 = input_2.split()
result_2 = kth_smallest_trimmed_number(nums_2, queries_2)
print("Exercise-2 Output:", " ".join(map(str, result_2)))
