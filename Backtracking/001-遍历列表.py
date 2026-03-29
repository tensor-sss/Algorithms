"""
@file   : 001-遍历列表.py
@time   : 2026-03-29
"""
# 遍历列表。 [12, [15, 32, [53, 23]], [564], 42]    # 输出: 12 15 32 53 23 564  42
def func1(l1):
    result = []
    def backtrack(l1):
        if type(l1) != list:
            result.append(l1)
            return
        for v in l1:
            backtrack(v)

    backtrack(l1)
    return result

l1 = [12, [15, 32, [53, 23]], [564], 42]
res = func1(l1)
print(res)    # [12, 15, 32, 53, 23, 564, 42]


'''
[12, [15, 32, [53, 23]], [564], 42]
                                          12                       result=[12]
                                  [15, 32, [53, 23]]  
                                                       15          result=[12, 15]
                                                       32          result=[12, 15, 32]
                                                    [53, 23]
                                                              53   result=[12, 15, 32, 53]
                                                              23   result=[12, 15, 32, 53, 23]
                                          [564]       
                                                      564          result=[12, 15, 32, 53, 23, 564]
                                            42                     result=[12, 15, 32, 53, 23, 564, 42]
'''

