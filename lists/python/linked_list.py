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

    def add(self, node):
        if self._is_empty():
            self.HEAD = node
            return node.value

        # find the end of the list
        curr = self.HEAD
        while curr.next != None:
            curr = curr.next

        # add the new node to the end of the list
        curr.next = node

        # return the value that was added for convenience
        return node.value

    def remove(self, value):
        if self.HEAD is None:
            return None

        if self.HEAD.value == value:
            removed = self.HEAD
            self.HEAD = self.HEAD.next
            return removed.value

        curr = self.HEAD
        while curr is not None:
            if curr.next is None and curr.value != value:
                # Not Found which idempotently means it was removed
                return None
            elif curr.next.value == value:
                removed = curr.next
                curr.next = curr.next.next
                return removed.value
            
            curr = curr.next

    def pop(self):
        if self.HEAD is None:
            return None

        item = self.HEAD.value
        self.HEAD = self.HEAD.next
        return item

    def push(self, node):
        if self._is_empty():
            self.HEAD = node
            return node.value

        node.next = self.HEAD
        self.HEAD = node.next


class DoublyLinkedList(List):
    def add(self, node):
        if self.HEAD is None:
            self.HEAD = node
            return

        curr = self.HEAD
        while curr.next is not None:
            curr = curr.next

        curr.next = node
        node.prev = curr

    def remove(self, value):
        # If the list is empty technically the value is removed
        if self.HEAD is None:
            return

        curr = self.HEAD
        while curr.value != value:
            curr = curr.next

        if curr.prev is None and curr.next is None:
            # Only one item in the list
            self.HEAD = None
        elif curr.prev is None and curr.next is not None:
            # first item in a populated list
            self.HEAD = curr.next
            self.HEAD.prev = None
        elif curr.prev is not None and curr.next is None:
            # last item in a populated list
            curr.prev.next = None
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev


class CircularList(List):
    def as_list(self):
        if self.HEAD is None:
            return []

        values = []
        curr = self.HEAD
        while curr.next != self.HEAD:
            values.append(curr.value)
            curr = curr.next

        # Since we stop when curr.next is HEAD we need to manually
        # append the last value to the end of the values list
        # otherwise we will always exclude the tail value
        values.append(curr.value)
        return values

    def add(self, node):
        if self.HEAD is None:
            self.HEAD = node
            node.prev = node
            node.next = node
            return node

        node.prev = self.HEAD.prev
        node.next = self.HEAD
        self.HEAD.prev.next = node
        self.HEAD.prev = node

        return node

    def remove(self, value):
        if self.HEAD is None:
            return None

        tail = self.HEAD.prev
        curr = self.HEAD
        while curr.value != value:
            if curr == tail:
                return None
            curr = curr.next

        if curr == curr.next:
            # only one item in the list
            self.HEAD = None
        elif curr.next == curr.prev:
            # 2 items in the list and special consideration needed for HEAD
            if curr == self.HEAD:
                self.HEAD = curr.next # Could be curr.prev
            curr.next.prev = curr.prev
            curr.prev.next = curr.next
        else:
            curr.next.prev = curr.prev
            curr.prev.next = curr.next

        return curr

def is_valid(subject: str) -> bool:
    items = LinkedList()
    for i in range(0, len(subject)):
        item = subject[i]
        if item in ['(', '{' ,'[']:
            items.push(Node(item))
        else:
            match = items.pop()
            if item == ')' and match != '(':
                return False
            elif item == '}' and match != '{':
                return False
            elif item == ']' and match != '[':
                return False

    return items._is_empty()
