"""
@file   : 004-全排列2.py
@time   : 2026-03-29
"""
# 全排列2.0版本。 输入一个有重复的列表: [1,  1, 3], 输出所有的全排列，不能有重复。
# 提示: 提前要对列表排序。
def func1(l1):
    l1.sort()

    result = []
    n = len(l1)

    def backtrack(l1, temp, is_visited):
        if len(temp) == n:  # if len(l1) == 0:   终止条件
            result.append(temp.copy())
            return

        for i in range(len(l1)):
            if is_visited[i]:
                continue

            if i > 0 and l1[i] == l1[i-1] and not is_visited[i-1]:
                continue

            is_visited[i] = True
            temp.append(l1[i])
            backtrack(l1, temp, is_visited)
            is_visited[i] = False
            temp.pop()  # 默认弹出最后一个元素

    is_visited = [False] * n   # [False, False, False]
    backtrack(l1, [], is_visited)
    return result


if __name__ == '__main__':
    l1 = [1, 1, 3, 6]
    res = func1(l1)
    print(res)
