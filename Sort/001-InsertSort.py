"""
@file   : 001-InsertSort.py
@time   : 2026-01-25
"""

# 从1号位置走，每次从当前这个位置的前一个位置开始 倒着走 如果前一个位置的值 比当前这个值 大
# 那就往后移动一位。否则 前面那个位置的+1号位置 就是当前这个值插入的位置
def insert_sort(l1):
    for i in range(1, len(l1)):
        temp = l1[i]
        j = i - 1
        while j >= 0 and l1[j] > temp:
            l1[j+1] = l1[j]
            j -= 1
        l1[j+1] = temp
    return l1


# 错误代码
# def insert_sort_v1(l1):
#     for i in range(1, len(l1)):
#         temp = l1[i]  # 54
#         j = i - 1   # j=1
#         while l1[j] > temp :    # j=0
#             l1[j+1] = l1[j]   # [54, 254, 254, 75, 25, 756, 256]
#             if j == 0:
#                 break
#             j -= 1
#
#         if j == 0:
#             l1[0] = temp
#         else:
#             l1[j+1] = temp
#         print(l1)
#     return l1

if __name__ == '__main__':
    l1 = [254, 23, 54, 75, 25, 756, 256]
    res = insert_sort(l1)
    print(res)

