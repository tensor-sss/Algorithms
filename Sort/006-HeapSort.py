"""
@file   : 006-HeapSort.py
@time   : 2026-02-01
"""

def sift(l1, low, high):
    i = low
    j = 2*i+1
    temp = l1[i]
    while j <= high:
        # 到底是左 还是右大
        if j < high and l1[j] < l1[j+1]:
            j += 1

        # 如果当前这个父节点 比孩子节点小 那就把
        if temp < l1[j]:
            l1[i] = l1[j]
            i = j
            j = 2 * i + 1
        else:
            # 当前父节点 比左右都大的时候 就结束调整
            break
    l1[i] = temp

def heap_sort(l1):
    # len(n) // 2 - 1
    # 大顶堆的调整
    for i in range(len(l1)//2-1, -1, -1):
        sift(l1, i, len(l1)-1)

    for i in range(len(l1)-1, -1, -1):
        temp = l1[i]
        l1[i] = l1[0]
        l1[0] = temp
        sift(l1, 0, i-1)
    return l1


if __name__ == '__main__':
    l1 = [43, 12, 64, 35, 867, 23, 75, 18, 42]
    res = heap_sort(l1)
    print(res)

