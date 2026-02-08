# 2. 实现快速排序算法，对数组进行降序排序。
def QuickSort_desc(l, left, right):
    if left >= right:
        return
    # 递减的逻辑大致与递增的相反
    i, j = left, right
    if left < right:
        temp = l[left]
        while i != j:
            while i < j and temp > l[j]:
                j -= 1

            if i < j:
                l[i] = l[j]
                i += 1

            while i < j and l[i] > temp:
                i += 1

            if i < j:
                l[j] = l[i]
                j -= 1

        l[i] = temp
    QuickSort_desc(l, left, i - 1)
    QuickSort_desc(l, i + 1, right)
    return l

if __name__ == '__main__':
    l = [3, 32, 2, 567, 342, 22, 6, 9]
    res = QuickSort_desc(l, 0, len(l) - 1)
    print(res)



