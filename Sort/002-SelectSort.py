"""
@file   : 002-SelectSort.py
@time   : 2026-01-25
"""

def select_sort(l1):
    for i in range(len(l1)):
        # 然后从i+1号位置  找后面有没有更小的  记录更小的那个值所在位置 为了等会和i位置的值交换
        min_value = l1[i]
        min_index = i
        for j in range(i+1, len(l1)):
            if l1[j] < min_value:
                min_value = l1[j]
                min_index = j
        if min_index != i:
            temp = l1[i]
            l1[i] = l1[min_index]
            l1[min_index] = temp
    return l1


if __name__ == '__main__':
    l1 = [254, 23, 54, 75, 25, 756, 256]
    res = select_sort(l1)
    print(res)
