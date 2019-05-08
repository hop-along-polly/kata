from .linked_list import LinkedList
from .node import Node


def test_linkedlist_construct_empty_list():
    subject = LinkedList()
    assert subject == []
