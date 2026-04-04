"""
@file   : 005-股票交易一次机会.py
@time   : 2026-04-04
"""
# 5. 有一个数组 [8, 3, 5, 10, 2, 1, 5, 2], 展示的每天的股票的价格。 你现在有一次买入和卖出的机会。 求你能赚到最多的钱是多少？
# 解法一: 暴力求解
"""
def func1(l1):
    max_value = -float('inf')
    for i in range(len(l1)):
        for j in range(i, len(l1)):
            temp = l1[j] - l1[i]
            if temp > max_value:
                max_value = temp
    return max_value


l1 = [8, 3, 5, 10, 2, 1, 5, 2]
res = func1(l1)
print(res)
"""

# 解法二: 动态规划
# [[0, 0], [0, 0]]
def func2(l1):
    dp = [[0, 0] for i in range(len(l1))]

    """
    # 第0天
    # dp[0][0] = 0   # 没有股票
    # dp[0][1] = -l1[0]   # 有股票

    # 第1天
    # 一、没有股票:
    # (1) 前一天就没有 今天也没买 dp[0][0]
    # (2) 前一天有股票 今天卖了  dp[0][1] + l1[1]
    # 二、有股票
    # (1) 前一天有股票 今天没卖  dp[0][1]
    # (2) 前一天没有股票 今天买了  -l1[1]
    """
    for i in range(len(l1)):
        if i == 0:
            dp[0][0] = 0
            dp[0][1] = -l1[i]
        else:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + l1[i])
            dp[i][1] = max(dp[i-1][1], -l1[i])
    return dp[-1][0]


l1 = [8, 3, 5, 10, 2, 1, 5, 2]
res = func2(l1)
print(res)  # 7




