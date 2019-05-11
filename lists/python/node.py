class Node:
    def __init__(self, value):
        """
        Creates an instance of a Node with the provided value without being linked to a next or prev node.

        "param val" The value being stored in this node.
        """
        self.value = value
        self.next = None
        self.prev = None
