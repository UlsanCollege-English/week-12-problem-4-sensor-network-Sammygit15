
## main.py
```python
def prim_mst(graph, start):
    """
    Build a minimum spanning tree (MST) using a Prim-style algorithm.

    graph: dict mapping node -> list of (neighbor, weight) pairs.
           The graph is undirected (neighbors listed in both directions).
    start: starting node for Prim's algorithm.

    Return:
        (mst_edges, total_cost)
        - mst_edges: list of (u, v, w) edges in the MST.
        - total_cost: sum of weights w in all MST edges.

    You may assume:
        - graph is connected.
        - start exists in graph.
    """
    # TODO Step 1: Describe in your own words what MST means.
    # TODO Step 2: Re-phrase this problem in a very simple sentence.
    # TODO Step 3: Decide on data structures: visited set, edge list, mst_edges list, total_cost.
    # TODO Step 4: Plan Prim's algorithm: how do you grow the tree from the start node?
    # TODO Step 5: Write pseudocode for your Prim loop.
    # TODO Step 6: Implement the code here based on your pseudocode.
    # TODO Step 7: Test with small graphs and draw them to check the MST.
    # TODO Step 8: Reason about the time complexity of your approach.

    raise NotImplementedError("prim_mst is not implemented yet")


if __name__ == "__main__":
    # Optional manual test
    sample_graph = {
        "G1": [("G2", 4), ("G3", 2)],
        "G2": [("G1", 4), ("G3", 3)],
        "G3": [("G1", 2), ("G2", 3)],
    }
    edges, cost = prim_mst(sample_graph, "G1")
    print("Sample MST edges:", edges)
    print("Total cost:", cost)
