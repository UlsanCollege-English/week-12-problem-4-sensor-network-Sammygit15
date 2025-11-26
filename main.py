def prim_mst(graph, start):
    """
    Build a Minimum Spanning Tree (MST) using Prim's algorithm with deterministic tie-breaking.
    """
    visited = set([start])
    mst_edges = []
    total_cost = 0

    # Candidate edges: (weight, origin, neighbor)
    candidate_edges = [(w, start, neighbor) for neighbor, w in graph[start]]

    while candidate_edges and len(visited) < len(graph):
        # Sort by weight, then origin node, then neighbor node to ensure deterministic behavior
        candidate_edges.sort(key=lambda x: (x[0], x[1], x[2]))
        w, u, v = candidate_edges.pop(0)

        if v in visited:
            continue

        mst_edges.append((u, v, w))
        total_cost += w
        visited.add(v)

        for neighbor, weight in graph[v]:
            if neighbor not in visited:
                candidate_edges.append((weight, v, neighbor))

    return mst_edges, total_cost
