import networkx as nx

class Graph(nx.Graph):
    """Undirected graph."""
    pass

class DiGraph(nx.DiGraph):
    """Directed graph."""
    pass

def shortest_path(G, source, target, weight=None):
    """Finds the shortest path."""
    return nx.shortest_path(G, source, target, weight=weight)

def minimum_spanning_tree(G, weight='weight'):
    """Finds the MST."""
    return nx.minimum_spanning_tree(G, weight=weight)

def bfs_tree(G, source):
    """Breadth-First Search."""
    return nx.bfs_tree(G, source)

def dfs_tree(G, source):
    """Depth-First Search."""
    return nx.dfs_tree(G, source)

def draw(G):
    """Draws the graph (requires matplotlib)."""
    nx.draw(G, with_labels=True)
