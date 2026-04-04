# 5. 输入两个整数 n 和 k,  返回 [1, 2, 3,...n]中所有可能k个数组合。

def combination(n, k):
    res = []
    nums = []
    for i in range(1, n + 1):
        nums.append(i)

    temp = []

    def backtrack(nums, temp):

        if len(temp) == k:
            x = temp.copy()
            x = sorted(x)
            if x not in res:
                res.append(x)
            return

        for i in range(len(nums)):
            temp.append(nums[i])
            backtrack(nums[:i] + nums[i + 1 :], temp)
            temp.pop()

    backtrack(nums, temp)
    return res




if __name__ == '__main__':

    res = combination(5, 3)
    print(res)
    print('*' * 100)
    res = combination(7, 5)
    print(res)
    print('*' * 100)