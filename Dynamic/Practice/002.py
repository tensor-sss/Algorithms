# 12. 背包问题(跟10题有点类似)
# 有n个物品和一个容量为C的背包。每个物品i都有重量s[i]和价值v[i]，其中1 ≤ i ≤ n。
# 需要选择一些物品放入背包，使得放入的物品总重量不超过背包容量C，且总价值最大。

def highest_value(s, v ,c, n):

    dp = [[0] * (n + 1) for _ in range(c + 1)]


    for i in range(1, c + 1):
        for j in range(1, n + 1):
            if i < s[j - 1]:
                dp[i][j] = dp[i][j - 1]

            else:
                dp[i][j] = max(dp[i - s[j - 1]][j - 1] + v[j - 1], dp[i][j - 1])
    return dp[c][n]


s = [2, 3, 4, 5]
v = [3, 4, 5, 8]
n = 4
c = 8

res = highest_value(s, v ,c, n)
print(res)

'''
[[0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0], 
[0, 3, 3, 3, 3], 
[0, 3, 4, 4, 4],
[0, 3, 4, 5, 5], 
[0, 3, 7, 7, 8], 
[0, 3, 7, 8, 8], 
[0, 3, 7, 9, 11], 
[0, 3, 7, 9, 12]]
'''
