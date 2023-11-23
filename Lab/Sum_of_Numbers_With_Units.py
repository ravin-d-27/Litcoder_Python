def sum_of_numbers_with_units(num, k):
    if num == 0:
        return 0
    for i in range(1, 11):  
        if num % 10 == ((i * k) % 10) and i*k<=num: 
            return i
        
    return -1
    
s = str(input()).split()

if " " not in s:
    print(-1)
else:
    num = int(s[0])
    k = int(s[1])
    print(sum_of_numbers_with_units(num,k))