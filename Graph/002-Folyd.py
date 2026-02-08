"""
@file   : 002-Folyd.py
@time   : 2026-02-08
"""
from pprint import pprint

def run_folyd(graph, path):
    num = len(graph)
    for i in range(num):
        # i=0  1 2 3 ....6
        # 0作为中间节点  然后检查两两节点之间的距离 能不能缩短
        # 如果能缩短 会更新graph中距离  会将对应path的位置 改成0
        for m in range(num):
            for n in range(num):
                if graph[m][i] + graph[i][n] < graph[m][n]:
                    graph[m][n] = graph[m][i] + graph[i][n]
                    path[m][n] = i
    return graph, path

def print_path(path, s, e):
    result = []
    def dfs(path, s, e):
        if path[s][e] == -1:
            result.append(s)
        else:
            mid = path[s][e]
            dfs(path, s, mid)
            dfs(path, mid, e)
    dfs(path, s, e)
    result += [e]
    return result


if __name__ == '__main__':
    inf = float('inf')
    graph = [
        [0,  4,   6,    6, inf, inf, inf],
        [inf,  0,   1,  inf,   7, inf, inf],
        [inf, inf,  0,  inf,   6,   4, inf],
        [inf, inf,  2,    0, inf,   5, inf],
        [inf, inf, inf, inf,   0, inf,   6],
        [inf, inf, inf, inf,   1,   0,   8],
        [inf, inf, inf, inf, inf, inf,   0]
    ]
    column_num = len(graph[0])
    rows_num = len(graph)
    path = []
    for i in range(rows_num):
        temp = [-1] * column_num
        path.append(temp)
    dist, path = run_folyd(graph, path)

    # 打印路径
    res = print_path(path, 0, 6)
    print(res)  # [0, 1, 2, 5, 4, 6]


