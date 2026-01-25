"""
@file   : 003-BubbleSort.py
@time   : 2026-01-25
"""

def bubble_sort(l1):
    # 两层for
    # 外层控制比较多少次
    for i in range(len(l1)-1, 0, -1):
        for j in range(i):  # range(6)
            if l1[j] > l1[j+1]:
                # temp = l1[j]
                # l1[j] = l1[j+1]
                # l1[j+1] = temp
                l1[j], l1[j+1] = l1[j+1], l1[j]
    # 1+2+3+...+n =>  (1+n)n/2
    return l1


def bubble_sort_v1(l1):
    # 外层控制比较多少次
    for i in range(len(l1)-1, 0, -1):
        is_label = True
        for j in range(i):  # range(6)
            if l1[j] > l1[j+1]:
                # temp = l1[j]
                # l1[j] = l1[j+1]
                # l1[j+1] = temp
                l1[j], l1[j+1] = l1[j+1], l1[j]
                is_label = False
        if is_label:
            break
    return l1


if __name__ == '__main__':
    # l1 = [254, 23, 54, 75, 25, 756, 256]
    l1 = [23, 25, 54, 75, 254, 256, 756]
    res = bubble_sort(l1)
    print(res)
    # [254, 23, 54, 75, 25, 756, 256]
    # [23, 254, 54, 75, 25, 756, 256]
    # [23, 54, 75, 254, 25, 756, 256]
    # [23, 54, 75, 25, 254, 756, 256]
    # [23, 54, 75, 25, 254, 756, 256]
    # [23, 54, 75, 25, 254, 256, 756]     # 保证最后一个值 目前是最大值

