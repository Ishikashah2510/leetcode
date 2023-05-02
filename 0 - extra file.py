def SubsetSum(S, i, T):
    if T == 0:
        return 1
    elif T < 0 or i == -1:
        return 0
    else:
        e = S[i]
        include = SubsetSum(S, i - 1, T - e)
        exclude = SubsetSum(S, i - 1, T)
        return include + exclude


# print(SubsetSum([1, 4, 3, 2, 5], 4, 6))


def print_matrix(matrix):
    print(*matrix, sep='\n')
    print('-'*25)


def DpSubsetSumUpdated(S, T):
    n = len(S) + 1
    result = [[0] * (T+1) for i in range(n)]

    print_matrix(result)

    for i in range(n):
        result[i][0] = 1
    for t in range(1, T+1):
        result[0][t] = 0

    print_matrix(result)

    for i in range(0, n-1):
        for t in range(1, S[i]):
            result[i][t] = result[i-1][t]

        for t in range(S[i], T):
            result[i][t] = result[i-1][t] + result[i-1][t-S[i]]

        print("Loop : ", i)
        print_matrix(result)

    print_matrix(result)

    return result[n-2][T-1]


# print(DpSubsetSumUpdated([1, 4, 3, 2], 7))


