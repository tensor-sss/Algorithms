# 6. 组合总和。有一个列表L1 = [1, 2, 4, 5, 8],   target=8, 找出L1中的元素  加和等于target所有组合。 注意: 这个列表中的数可以重复利用。

def combination(l, target):
    res = []
    temp = []
    def backtrack(l,temp, is_visited):

        if sum(temp) == target:
            res.append(temp.copy())
            return

        if sum(temp) > target:
            return

        for i in range(len(l)):

            if is_visited[i]:
                continue



            temp.append(l[i])
            #is_visited[i] = True
            backtrack(l,temp, is_visited)
            temp.pop()
            #is_visited[i] = False


    is_visited = [False] * len(l)
    backtrack(l, temp, is_visited)
    return res


if __name__ == '__main__':
    l1 = [1, 2, 4, 5, 8]
    target=8
    res = combination(l1, target)
    print(res)