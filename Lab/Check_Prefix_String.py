def Check_Prefix_of_String(lst):
    
    record = sorted(lst)
    char = record[0][0]
    del record[0]
    
    for i in record:
        if i[0]==char:
            return "BAD PASSWORD"
    
    return "GOOD PASSWORD"
    
lst = input().split()
print(Check_Prefix_of_String(lst))