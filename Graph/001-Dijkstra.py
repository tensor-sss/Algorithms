"""
@file   : 001-Dijkstra.py
@time   : 2026-02-01
"""


def dijkstra(graph, v):
    inf = float('inf')
    dist = [inf] * len(graph)
    path = [-1] * len(graph)
    visit = [0] * len(graph)

    # 初始化
    visit[v] = 1
    for i in range(0, len(graph)):
        distance = graph[v][i]
        dist[i] = distance
        if distance < inf:
            path[i] = v
    # print(path)  # [-1, 0, 0, 0, -1, -1, -1]
    # print(dist)  # [inf, 4, 6, 6, inf, inf, inf]

    for i in range(len(graph)-1):
        # 从dist找出最短距离  以及对应的节点编号
        min_distance = inf
        u = inf
        for j in range(len(graph)):
            if visit[j] == 0 and dist[j] < min_distance:
                u = j
                min_distance = dist[j]
        visit[u] = 1
        for j in range(len(graph)):
            if visit[j] == 0 and dist[u] + graph[u][j] < dist[j]:
                dist[j] = dist[u] + graph[u][j]
                path[j] = u
    return dist, path


# 邻接矩阵
if __name__ == '__main__':
    inf = float('inf')
    graph = [
        [inf,  4,   6,    6, inf, inf, inf],
        [inf,  inf,   1,  inf,   7, inf, inf],
        [inf, inf,  inf,  inf,   6,   4, inf],
        [inf, inf,  2,    inf, inf,   5, inf],
        [inf, inf, inf, inf,   inf, inf,   6],
        [inf, inf, inf, inf,   1,   inf,   8],
        [inf, inf, inf, inf, inf, inf,   inf]
    ]
    dist, path = dijkstra(graph, v=0)  # v:起始节点
    print(dist)
    print(path)





