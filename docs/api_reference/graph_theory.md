# API Reference: Graph Theory

## Module: `anvaya.graph_theory`

---

## Classes

### `Graph`
Creates an undirected graph (inherits from `networkx.Graph`).

### `DiGraph`
Creates a directed graph (inherits from `networkx.DiGraph`).

---

## Functions

### `shortest_path`

```python
shortest_path(G: Graph, source: Any, target: Any, weight: str = None) -> list
```

Finds the shortest path between two nodes.

| Parameter | Type | Description |
|-----------|------|-------------|
| `G` | `Graph` | Input graph |
| `source` | `Any` | Starting node |
| `target` | `Any` | End node |
| `weight` | `str` | Edge attribute to use as weight |

---

### `minimum_spanning_tree`

```python
minimum_spanning_tree(G: Graph) -> Graph
```

Computes the Minimum Spanning Tree (MST) of the graph.

---

### `bfs_tree` / `dfs_tree`

```python
bfs_tree(G: Graph, source: Any) -> Graph
dfs_tree(G: Graph, source: Any) -> Graph
```

Returns the Breadth-First or Depth-First search tree starting from a node.

---

### `draw`

```python
draw(G: Graph)
```

Renders a visual representation of the graph (requires `matplotlib`).
