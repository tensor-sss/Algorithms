# 7. 组合总和2.0。有一个列表L1 = [1, 2, 4, 5, 8],   target=8, 找出L1中的元素  加和等于target所有组合。 注意: 这个列表中的数不可以重复利用。
def sum1(l, target):
    res = []
    temp = []
    def backtrack(l, temp):
        if sum(temp) == target:
            res.append(temp.copy())
            return

        if sum(temp) > target:
            return

        for i in range(len(l)):
            temp.append(l[i])
            backtrack(l[:i] + l[i+1:], temp)
            temp.pop()
    backtrack(l, temp)
    return res




if __name__ == '__main__':
    l = [1, 2, 4, 5, 8]
    target=8
    res = sum1(l, target)
    print(res)