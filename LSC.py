def display_LCS(D, X, i, j):
    if i == 0 or j == 0:
        print(end=" ")
    elif D[i][j] == "D":
        display_LCS(D, X, i - 1, j - 1)
        print(X[i - 1], end=" ")
    elif D[i][j] == "U":
        display_LCS(D, X, i - 1, j)
    else:
        display_LCS(D, X, i, j - 1)


def LCS(X, Y):
    m = len(X)
    n = len(Y)

    C = [[0 for i in range(n + 1)] for i in range(m + 1)]
    D = [[" " for i in range(n + 1)] for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                C[i][j] = 0
                D[i][j] = "-"
            elif X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
                D[i][j] = "D"
            elif C[i - 1][j] >= C[i][j - 1]:
                C[i][j] = C[i - 1][j]
                D[i][j] = "U"
            else:
                C[i][j] = C[i][j - 1]
                D[i][j] = "L"

    print("Table C for computing Length Of LCS :-")
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            print(C[i][j], end='\t')
        print()
    print("The Length Of LCS is", C[m][n])

    print("Table D for Direction Of LCS :-")
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            print(D[i][j], end='\t')
        print()

    print("Longest Common Subsequnce :- ", end=" ")
    display_LCS(D, X, m, n)


X = "pqrstpqrs"
Y = "pratpbrqrps"
LCS(X, Y)
