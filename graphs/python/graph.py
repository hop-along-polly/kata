class NodeDoesNotExistException(Exception):
    """
    You will not need to modify this it is provided as an example
    of how you define a custom exception.
    """
    pass


class Graph:
    """
    Implement an Undirectional Graph
    """
    class Node:
        """
        Implement a Graph Node. This is a subclass, since this node is
        very specific for the graph implementation and should not be used
        elsewhere in the code base.
        """
        def __init__(self, id: str, weight: int, **kwargs):
            pass

    def __init__(self, nodes: list = None):
        pass
