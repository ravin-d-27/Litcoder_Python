def maximize_Number_Of_Subsequences(text, pattern):
    ans = 0;
    x = 0;
    y = 0;
    for i in text:
        if i==pattern[1]:
            ans+=x
            y+=1
        
        if i==pattern[0]:
            x+=1
    final = max(x,y)
    return ans+final
            


print(maximize_Number_Of_Subsequences('ababab','ab'))
