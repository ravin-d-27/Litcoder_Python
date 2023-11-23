def calc(lst):
    lst = sorted(lst)
    sweet = lst[0] + 2 * lst[1]
    lst.pop(1)
    lst.pop(0)
    lst.append(sweet)
    return sweet, lst

def sweetness(candies, target):
    ans = 0
    c = 0

    while True:
        ans, candies = calc(candies)
        c += 1

        if candies[0]>target:
            break;

    return c

print(sweetness([1,2,3,4,5], 7))
