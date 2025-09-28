import heapq


def dijkstra_all_paths(graph, src, dest):
    """
    Dijkstra's algorithm on a weighted adjacency matrix.
    Returns all equally shortest paths from src to dest.

    :param graph: 2D list adjacency matrix (graph[u][v] = weight or float('inf') if no edge)
    :param src: source vertex index
    :param dest: destination vertex index
    :return: (distance, all_paths)
    """
    n = len(graph)
    dist = [float('inf')] * n
    prev = [[] for _ in range(n)]  # store all predecessors
    visited = [False] * n

    dist[src] = 0
    pq = [(0, src)]  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True

        for v in range(n):
            if graph[u][v] != 0 and graph[u][v] != float('inf'):  # edge exists
                new_dist = dist[u] + graph[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    prev[v] = [u]  # reset predecessors
                    heapq.heappush(pq, (new_dist, v))
                elif new_dist == dist[v]:
                    prev[v].append(u)  # add additional predecessor

    # recursively reconstruct all shortest paths
    def build_paths(node):
        if node == src:
            return [[src]]
        paths = []
        for p in prev[node]:
            for sp in build_paths(p):
                paths.append(sp + [node])
        return paths

    all_paths = build_paths(dest) if dist[dest] != float('inf') else []
    return dist[dest], all_paths



