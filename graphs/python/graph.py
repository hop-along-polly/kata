import string

from typing import List

class NodeDoesNotExistException(Exception):
    pass


class Graph:
    """
    Nodes should be maintaining their, own ID, but after being added
    the graph should ensure a node with a duplicate ID is not added.
    """
    class Node:
        def __init__(self, id: str, weight: int, **kwargs):
            self.id = id
            self.weight = weight
            self.neighbors = kwargs.get('neighbors', [])

        def add_neighbor(self, neighbor):
            self.neighbors.append(neighbor)

        def remove_neighbor(self, neighbor_id):
            self.neighbors = [n for n in self.neighbors if n.id != neighbor_id]

    def __init__(self, nodes: list = None):
        self.node_map = {}
        self._distances = {}
        self._visited = []
        nodes = [] if nodes is None else nodes
        for node in nodes:
            try:
                self.add(node.id, node.weight, neighbors=[neighbor.id for neighbor in node.neighbors])
            except KeyError:
                pass

    @property
    def empty(self):
        return len(self.node_map) == 0

    @property
    def nodes(self):
        return [ n for n_id, n in self.node_map.items()]

    @classmethod
    def create(cls, matrix = None):
        if not matrix or not matrix[0]:
            return cls([])

        nodes = []
        matrix_copy = [row[:] for row in matrix]
        for i in range(len(matrix_copy)):
            for j in range(len(matrix_copy[i])):
                # If I need to dynamically choose the id
                node = Graph.Node(
                    matrix_copy[i][j][0], # maps to nodes ID
                    matrix_copy[i][j][1] # maps to nodes weight
                )
                matrix_copy[i][j] = node
                nodes.append(node)

                # horizontal relationships
                if j > 0:
                    node.add_neighbor(matrix_copy[i][j-1])
                    matrix_copy[i][j-1].add_neighbor(node)
                # # vertical relationships
                if i > 0:
                    node.add_neighbor(matrix_copy[i-1][j])
                    matrix_copy[i-1][j].add_neighbor(node)

        return cls(nodes)

    def add(self, node_id: str, weight: int, neighbors: list=None) -> Node:
        """
        Adds a node to the existing graph with associated neighbors
        Not sure what I want neighbors to be yet.
        """
        
        if node_id in self.node_map:
            return self.node_map[node_id]

        self.node_map[node_id] = Graph.Node(node_id, weight) # Ah I like this cause now I could add a vistied flag to the node....well if I need a visted flag.

        if neighbors is None:
            # If no neighbors were provided go ahead an exit early.
            return self.node_map[node_id]

        for n in neighbors:
            self.node_map[node_id].add_neighbor(self.node_map[n])
            self.node_map[n].add_neighbor(self.node_map[node_id])

        return self.node_map[node_id]

    def remove(self, node_id: str) -> Node:
        if node_id not in self.node_map:
            # Returning true, since if the node wasn't found then technically it's removed
            return True

        removed = self.node_map.pop(node_id)
        for neighbor in removed.neighbors:
            neighbor.remove_neighbor(node_id)

        return removed

    def _visit(self, node: Node):
        self._visited.append(node.id)
        path_cost = self._distances[node.id]
        for neighbor in node.neighbors:
            if neighbor.id not in self._distances:
                # Always record the first time a node is seen
                self._distances[neighbor.id] = path_cost + neighbor.weight
            elif neighbor.weight + path_cost < self._distances[neighbor.id]:
                # Found a shorter path...log it
                self._distances[neighbor.id] = neighbor.weight + path_cost

        node.neighbors.sort(key=lambda x: x.weight)
        for neighbor in node.neighbors:
            if neighbor.id not in self._visited:
                self._visit(neighbor)

    def djikstra(self, source):
        if source not in self.node_map:
            raise NodeDoesNotExistException(f'A node with id {source} does not exist in the graph')

        start = self.node_map[source]
        self._distances = { start.id: 0 }
        self._visit(start)

        return self._distances
