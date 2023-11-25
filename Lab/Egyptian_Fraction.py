
import math

def egyptianFraction(nr, dr):
    ef = []
    while nr != 0:
        x = math.ceil(dr / nr)
        ef.append(x)
        nr = x * nr - dr
        dr = dr * x
    
    return ef


n1 = int(input())
n2 = int(input())
ef = egyptianFraction(n1, n2)
for i in ef:
    print(i)