"""
@file   : 006-股票交易不限次数.py
@time   : 2026-04-04
"""
# 解法二: 动态规划
# [[0, 0], [0, 0]]
def func2(l1):
    dp = [[0, 0] for i in range(len(l1))]
    for i in range(len(l1)):
        if i == 0:
            dp[0][0] = 0
            dp[0][1] = -l1[i]
        else:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + l1[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - l1[i])
    return dp[-1][0]


l1 = [8, 3, 5, 10, 2, 1, 5, 2]
res = func2(l1)
print(res)  # 7

