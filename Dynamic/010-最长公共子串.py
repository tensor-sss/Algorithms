"""
@file   : 010-最长公共子串.py
@time   : 2026-04-05
"""
def func1(text1, text2):
    dp = [[0] * (len(text1) + 1) for _ in range(len(text2)+1)]

    max_value = 0
    for i in range(1, len(text2)+1):
        for j in range(1, len(text1) + 1):
            if text2[i-1] == text1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_value:
                    max_value = dp[i][j]
            else:
                dp[i][j] = 0
    return max_value
'''
[[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 1, 0, 0, 0, 1, 0], 
 [0, 0, 0, 2, 0, 0, 0, 2], 
 [0, 0, 0, 0, 3, 0, 0, 0], 
 [0, 0, 0, 0, 0, 4, 0, 0], 
 [0, 0, 1, 0, 0, 0, 5, 0],
 [0, 0, 0, 2, 0, 0, 0, 6], 
 [0, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0]]
'''

text1 = "wasdfas"
text2 = "werasdfaswer"
res = func1(text1, text2)
print(res)

