from abc import ABC

from .node import Node


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
    """
    Implement a Singly Linked List Here
    """


class DoublyLinkedList(List):
    """
    Implement a Double Linked List Here
    """


class CircularList(List):
    """
    Implement a Circularly Linked List Here
    """
