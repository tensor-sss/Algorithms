"""
@file   : 002-求连续子数组的最大和.py
@time   : 2026-04-04
"""

# 2. 最大连续子数组的和
# 给你一个列表， 找出连续子数组的和，返回最大的和。
# [2, 4 -1, 8, 7, -9, 4, -2, 11, 4, -2]
def func1(l1):
    max_value = -float('inf')
    for i in range(len(l1)):
        for j in range(i+1, len(l1)):
            sub = l1[i:j]
            if sum(sub) > max_value:
                max_value = sum(sub)
    return max_value


def func2(l1):
    dp = [0] * len(l1)
    dp[0] = l1[0]
    for i in range(1, len(l1)):
        # 第1个值:  4   case1: 连续  case2: 不连续
        temp = dp[i-1] + l1[i]  # dp[0] + l1[1]
        dp[i] = max(temp, l1[i])
    # print(dp)  # [2, 6, 5, 13, 20, 11, 15, 13, 24, 28, 26]
    return max(dp)


l1 = [2, 4, -1, 8, 7, -9, 4, -2, 11, 4, -2]
res1 = func1(l1)
res2 = func2(l1)
# print(res1)
# print(res2)

# l1 = [2, 4, -1, 8, 7, -9, 4, -2, 11, 4, -2]
# dp = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# loop1: dp=[2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0]     max(6, 4) => 6
# loop2: dp=[2, 6, 5, 0, 0, 0, 0, 0, 0, 0, 0]     max(5, -1) => 5
# loop3: dp=[2, 6, 5, 13, 0, 0, 0, 0, 0, 0, 0]    max(13, 8) => 13
# loop4: dp=[2, 6, 5, 13, 0, 0, 0, 0, 0, 0, 0]
