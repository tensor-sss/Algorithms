"""
@file   : 001-斐波那契数列.py
@time   : 2026-04-04
"""

"""
def func1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return func1(n-1) + func1(n-2)

res = func1(8)
print(res)
"""

# 动态规划的解法
def func2(n):
    if  n == 1:
        return 0
    if  n == 2:
        return 1
    a, b = 0, 1
    for i in range(n-2):
        a, b = b, a + b
    return b


def func3(n):
    if  n == 1:
        return 0
    if  n == 2:
        return 1

    dp = [0] * n
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

res = func2(5)
print(res)

res = func3(5)
print(res)














