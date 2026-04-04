"""
@file   : 003-求路径条数.py
@time   : 2026-04-04
"""



def func1(m, n):
    dp = [[0] * n for _ in range(m)]
    # print(dp)
    # [[0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0]]

    for i in range(m):
        dp[i][0] = 1

    for i in range(n):
        dp[0][i] = 1


    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]


res = func1(3, 5)
print(res)

