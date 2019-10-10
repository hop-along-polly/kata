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
            return node
        
        # Find the end of the list
        curr = self.HEAD
        while curr.next is not None:
            curr = curr.next

        # Link the node to the end of the list
        curr.next = node

        return node

   
    def remove(self, node):
        if self._is_empty():
            return None

        # Remove node if first node
        if self.HEAD.value == node.value:
            self.HEAD = self.HEAD.next
            return node


        elif self.HEAD.value is not node.value:
            curr = self.HEAD.next
            previous = self.HEAD
            while curr is not None:
                if(curr.value == node.value):
                    previous.next = curr.next
                    return node
                elif curr is not node.value:
                    curr = curr.next
                    previous = previous.next
            return None

   
class DoublyLinkedList(List):
    # Add to the end   
    def add(self, node):
        # Check to see if if list is empty
        if self.HEAD is None:
            self.HEAD = node
            return node.value
        
        # Find last node
        curr = self.HEAD
        while curr.next is not None:
            curr = curr.next
        
        # Attach new node to end of list
        curr.next = node
        node.prev = curr
        return node.value
    
    def remove(self,value):
        if self.HEAD is None:
            return None

        # Remove node if first node
        elif self.HEAD.value is value:
            # Check to see if there is only one node
            if self.HEAD.next is None:
                self.HEAD = None

            else:
                self.HEAD = self.HEAD.next
                self.HEAD.prev = None
                return value    

        curr = self.HEAD.next
        while curr.value is not value:
            if curr is None:
                return None
            curr = curr.next

        curr.prev.next = curr.next

        if curr.next is not None: 
            curr.next.prev = curr.prev

        return value   

class CircularList(List):
    # Add to the end   
    def add(self, node):
        pass
    #     if self.HEAD is None:
    #         self.HEAD = node
    #         node.next = node
    #         return node.value
        
    #     # Find the end of the list
    #     curr = self.HEAD
    #     while curr.next is not self.HEAD:
    #         curr = curr.next

    #     # Link the node to the end of the list
    #     curr.next = node

    #     return node.value
    def remove(self,value):
        pass

def is_valid(subject: str) -> bool:
    """
    Implement the is_valid function using the push and pop methods on the LinkedList
    class
    """