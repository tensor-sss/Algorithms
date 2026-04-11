# 9. 给你一个整数数组 nums，数组中的元素互不相同。返回该数组所有可能的子集。解集不能包含重复的子集。你可以按任意顺序返回解集。
def sub_list(l):
    res = [[]]
    def backtrack(l, temp, is_visited):
        if temp not in res:
            res.append(temp.copy())

        if len(temp) == len(l):
            res.append(temp.copy())
            return

        for i in range(len(l)):
            if not is_visited[i]:
                temp.append(l[i])
                backtrack(l, temp, is_visited)
                temp.pop()
                is_visited[i] = True


    is_visited = [False] * len(l)
    backtrack(l, [], is_visited)
    return res

l = [1, 2, 3]
res = sub_list(l)
print(res)