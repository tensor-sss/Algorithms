"""
@file   : 002-全排列.py
@time   : 2026-03-29
"""

# 2. 全排列， 传入一个没有重复元素的列表: [1, 2, 3]   => 6个列表  [1, 2, 3] [1, 3, 2], [2, 1, 3], [2, 3, 1],  [3, 1, 2],  [3, 2, 1]
def func1(l1):
    result = []
    n = len(l1)

    def backtrack(l1, temp):
        if len(temp) == n:  # if len(l1) == 0:   终止条件
            result.append(temp.copy())
            return

        for i in range(len(l1)):
            temp.append(l1[i])
            backtrack(l1[:i] + l1[i + 1:], temp)
            temp.pop()  # 默认弹出最后一个元素

    backtrack(l1, [])
    return result


if __name__ == '__main__':
    l1 = [1, 2, 3]
    res = func1(l1)
    print(res)
'''
[1, 2, 3]  
           1    backtrack([2, 3], [1])
                                        2   backtrack([3], [1, 2])
                                                                    3   backtrack([], [1, 2, 3])

                                        3   backtrack([2], [1, 3])                            


'''