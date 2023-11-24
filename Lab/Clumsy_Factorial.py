def clumsy_fact(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6

    result = n * (n - 1) // (n - 2) + (n - 3)

    n -= 4
    while n >= 4:
        result -= n * (n - 1) // (n - 2) - (n - 3)
        n -= 4

    if n == 1:
        return result - 1
    elif n == 2:
        return result - 2
    elif n == 3:
        return result - 6
    else:
        return result

print(clumsy_fact(int(input())))