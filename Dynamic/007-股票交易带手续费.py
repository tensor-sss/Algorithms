"""
@file   : 007-股票交易带手续费.py
@time   : 2026-04-05
"""
# 8. 有一个数组 [8, 3, 5, 10, 2, 1, 5, 2], 展示的每天的股票的价格。 你现在无数次买入和卖出的机会。
# 求你能赚到最多的钱是多少？   同一时间只能做一笔交易。  冷冻期1天。
# 每次交易收取手续费1元   不管是买 还是卖 都会收取费用
def func2(l1, fea):
    dp = [[0, 0] for i in range(len(l1))]
    for i in range(len(l1)):
        if i == 0:
            dp[0][0] = 0
            dp[0][1] = -l1[i] - fea
        elif i == 1:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + l1[i] - fea)
            dp[i][1] = max(dp[i-1][1], -l1[i] - fea)
        else:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + l1[i] - fea)
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - l1[i] - fea)
    return dp[-1][0]


l1 = [8, 3, 5, 10, 2, 1, 5, 2]
fea = 1
res = func2(l1, fea)
print(res)  # 7
