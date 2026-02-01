def sort(l1, left, right):

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

            # 从最左边  往右走
            while i < j and l1[i] < temp:
                i += 1
            if i < j:
                l1[j] = l1[i]
                j -= 1
        l1[i] = temp

    return i

def find_kth_largest(l, k):

    left, right = 0, len(l) - 1
    target = len(l) - k

    while left <= right:

        num = sort(l, left, right)

        if num == target:
            return l[num]
        elif num < target:
            left = num + 1
        else:
            right = num - 1

if __name__ == '__main__':
    l1 = [84, 23, 54, 19, 190, 25, 756, 85, 256]
    print(find_kth_largest(l1, 3))
