# Graph Theory Module

The `graph_theory` module provides graph structures and algorithms using NetworkX.

---

## Import

```python
from anvaya import graph_theory as gt
```

---

## Classes

### `Graph`
Undirected graph (extends `networkx.Graph`).

```python
G = gt.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])
```

### `DiGraph`
Directed graph (extends `networkx.DiGraph`).

```python
G = gt.DiGraph()
G.add_edges_from([(1, 2), (2, 3)])
```

---

## Functions

### `shortest_path(G, source, target, weight=None)`
Finds shortest path between nodes.

```python
G = gt.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])
path = gt.shortest_path(G, 1, 4)  # [1, 2, 3, 4]
```

---

### `minimum_spanning_tree(G, weight='weight')`
Finds minimum spanning tree.

```python
G = gt.Graph()
G.add_weighted_edges_from([(1, 2, 1), (2, 3, 2), (1, 3, 3)])
mst = gt.minimum_spanning_tree(G)
```

---

### `bfs_tree(G, source)`
Breadth-First Search tree.

```python
tree = gt.bfs_tree(G, 1)
```

---

### `dfs_tree(G, source)`
Depth-First Search tree.

```python
tree = gt.dfs_tree(G, 1)
```

---

### `draw(G)`
Visualizes the graph (requires matplotlib).

```python
gt.draw(G)
```

---

## See Also

- [Discrete Mathematics](discrete.md)
