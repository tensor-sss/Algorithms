"""
@file   : 003-组合串.py
@time   : 2026-03-29
"""
# [['a', 'b', 'c'], ['z', 'q'], ['d', 'm']]   写有所有的组合。
# 'azd', 'azm', 'aqd', 'aqm', 'bzd', 'bzm', ....
def func1(l1):
    result = []
    def backtrack(l1, temp):
        if len(l1) == 0:
            result.append(temp)
            return
        for v in l1[0]:
            temp = temp+ v
            backtrack(l1[1:], temp)
            temp = temp[:-1]
    backtrack(l1, '')
    return result

if __name__ == '__main__':
    l1 = [['a', 'b', 'c'], ['z', 'q'], ['d', 'm']]
    res = func1(l1)
    print(res)