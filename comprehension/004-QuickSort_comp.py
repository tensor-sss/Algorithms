# 快排的核心逻辑


def QuickSort(l, left, right):

    # 终止条件，left >= right
    if left >= right:
        return

    i = left
    j = right

    if left < right:

        temp = l[left]
        # 当i = j时，说明整个列表遍历完成
        while i != j:
            # 因为起始时目标值与left节点在一起，所以先从右边走
            while i < j and temp < l[j]:
                j -= 1
            #@ 通过左右交替扫描，把 < temp 的值移动到左边坑，把 > temp 的值移动到右边坑
            # 当while循环结束时，说明遇见比temp小的值
            if i < j:
                # 将比temp小的值移动到i处
                l[i] = l[j]
                # 此时i位置的值已经经过处理，所以我们将它向后移位
                i += 1

            # 接下来从左往右走，找比temp大的值
            while i < j and temp > l[i]:
                i = i + 1

            if i < j:
                l[j] = l[i]
                j -= 1

        # 当i = j时候，说明一轮遍历完成，我们将temp的值放在i = j的位置，就可以确保左边都是比temp小的值，右边都是大的
        l[i] = temp
    # 此时temp的位置已经确定，只需要递归两边的值即可完成整个数组的排序
    QuickSort(l, left, i - 1)
    QuickSort(l, i + 1, right)
    return l

if __name__ == "__main__":
    l = [5, 4, 3, 2, 1]
    res = QuickSort(l, 0, len(l) - 1)
    print(res)





