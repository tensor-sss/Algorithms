"""
@file   : 004-QuickSort.py
@time   : 2026-01-25
"""

# medium hard
# 找出列表中第k大的值  要求时间复杂度尽可能能的低   log(n)    使用快排
def quick_sort(l1, left, right):
    if left >= right:
        return

    i, j = left, right
    if left < right:
        temp = l1[left]
        while i != j:
            # 从最右边 往左走
            while i < j and l1[j] > temp:
                j -= 1
            if i < j:
                l1[i] = l1[j]
                i += 1

            # 从最左白  往右走
            while i < j and l1[i] < temp:
                i += 1
            if i < j:
                l1[j] = l1[i]
                j -= 1
        l1[i] = temp
    quick_sort(l1, left, i-1)
    quick_sort(l1, i+1, right)
    return l1


if __name__ == '__main__':
    l1 = [84, 23, 54, 19, 190, 25, 756, 85, 256]
    res = quick_sort(l1, 0, len(l1)-1)
    print(res)

    # [84, 23, 54, 19, 25, 756, 85, 256]
    # 第一步: temp=84
    # [x, 23, 54, 91, 85, 19, 25, 756, 256]
    # [25, 23, 54, 91, 85, 19, x, 756, 256]
    #               i          j
    # [25, 23, 54, x, 85, 19, 91, 756, 256]
    #                      j
    # [25, 23, 54, 19, 85, x, 91, 756, 256]
    # [25, 23, 54, 19, x, 85, 91, 756, 256]
    #                  i
    # [25, 23, 54, 19, 84, 85, 91, 756, 256]
    #
