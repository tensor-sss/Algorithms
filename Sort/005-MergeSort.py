"""
@file   : 005-MergeSort.py
@time   : 2026-01-25
"""


# 归并排序
def merge(left, right):
    i = 0    # 负责left
    j = 0    # 负责 right
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):  # i没有走到头
        result.extend(left[i:])

    if j < len(right):
        result.extend(right[j:])
    return result


def merge_sort(l1):
    if len(l1) <= 1:
        return l1

    mid = len(l1) // 2
    left  = merge_sort(l1[:mid])
    right = merge_sort(l1[mid:])

    # merge合并
    result = merge(left, right)
    return result
# [84, 23, 54, 19, 190, 25, 756, 85, 256]
#         - [84, 23, 54, 19]
#              - [84, 23]
#                left=[84]  right=[23] => merge() => [23, 84]
#              - [54, 19]
#                left=[54]  right=[19] => merge() => [19, 54]
#              - merge()
#                left=[23, 84] right=[19, 54] => [19, 23, 54, 84]
#         - [190, 25, 756, 85, 256]
#             。。。。

if __name__ == '__main__':
    l1 = [84, 23, 54, 19, 190, 25, 756, 85, 256]
    res = merge_sort(l1)
    print(res)





