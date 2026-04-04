"""
@file   : 004-带障碍求路径条数.py
@time   : 2026-04-04
"""
# 求路径的条数，只能往下或往右走。  如果值为0 代表可以走  值为1 代表是障碍 不能走


def func1(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0] * n for _ in range(m)]

    # 列
    for i in range(m):
        if matrix[i][0] == 1:
            break
        dp[i][0] = 1

    # 行
    for i in range(n):
        if matrix[0][i] == 1:
            break
        dp[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # print(dp)
    # [[1, 1, 0, 0, 0],
    # [1, 2, 2, 0, 0],
    # [0, 0, 2, 2, 2]]
    return dp[-1][-1]


matrix = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]
res = func1(matrix)
print(res)




