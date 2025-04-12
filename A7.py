import heapq

def prim_mst(graph):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, 0)] 
    mst_cost = 0
    edges = []

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += cost

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))
                edges.append((u, v, weight))

    return mst_cost, edges

graph = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8)],
    [(1, 5), (2, 7)]
]

mst_cost, mst_edges = prim_mst(graph)
print("Cost of the Minimum Spanning Tree:", mst_cost)
print("Edges in the Minimum Spanning Tree:", mst_edges)