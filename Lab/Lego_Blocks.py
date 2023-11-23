def Lego_Blocks(x, y):
    MOD = 1000000007
    result = [0] * (y + 1)
    aux = [0] * (y + 1)

    aux[0] = 1
    for j in range(1, y + 1):
        aux[j] += aux[j - 1] if j - 1 >= 0 else 0; aux[j] += aux[j - 2] if j - 2 >= 0 else 0
        aux[j] += aux[j - 3] if j - 3 >= 0 else 0; aux[j] += aux[j - 4] if j - 4 >= 0 else 0

    for j in range(1, y + 1):
        aux[j] = aux[j] % MOD
        aux[j] = aux[j] ** x; aux[j] = aux[j] % MOD

    result[1] = 1
    for j in range(2, y + 1):
        result[j] = aux[j]
        for k in range(1, j):
            result[j] -= result[k] * aux[j - k]
        result[j] = result[j] % MOD

    return result[y] % MOD


# Example usage
print(Lego_Blocks(2, 2))  # Output: 3
print(Lego_Blocks(4, 4))  # Output: 3375
