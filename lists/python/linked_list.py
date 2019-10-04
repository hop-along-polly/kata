from abc import ABC

from .node import Node
from .exceptions import NodeNotFoundException

class List(ABC):
    def __init__(self):
        self.HEAD = None

    def as_list(self):
        if self.HEAD is None:
            return []

        values = []
        curr = self.HEAD
        while curr is not None and curr:
            values.append(curr.value)
            curr = curr.next

        return values

    def __eq__(self, other):
        return self.as_list() == other


class LinkedList(List):
    def _is_empty(self):
        return self.HEAD is None

    # Add to the end   
    def add(self, node):
        if self._is_empty():
            self.HEAD = node
            return node.value
        
        # Find the end of the list
        curr = self.HEAD
        while curr.next is not None:
            curr = curr.next

        # Link the node to the end of the list
        curr.next = node

        return node

   
    def remove(self, value):
        if self._is_empty():
            return None

        # Remove node if first node
        if self.HEAD.value is value:
            self.HEAD = self.HEAD.next
            return value


        elif self.HEAD.value is not value:
            curr = self.HEAD.next
            previous = self.HEAD
            while curr is not None:
                if(curr.value == value):
                    previous.next = curr.next
                    return value
                elif curr is not value:
                    curr = curr.next
                    previous = previous.next
            return None


class DoublyLinkedList(List):
    """
    Implement a Double Linked List Here
    """


class CircularList(List):
    """
    Implement a Circularly Linked List Here
    """
