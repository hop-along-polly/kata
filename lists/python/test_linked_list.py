import pytest

from .linked_list import LinkedList
from .node import Node
from .exceptions import NodeNotFoundException


def test_ll_construct_empty_list():
    subject = LinkedList()
    assert subject == []


def test_ll_add_to_empty_list():
    # arrange
    subject = LinkedList()
    node = Node('a')

    # act
    actual = subject.add(node)

    # assert
    assert actual == 'a'
    assert subject == ['a']


def test_ll_add_to_populated_list():
    # arrange
    subject = LinkedList()

    # setup the nodes to add
    existing_node = Node('existing')
    new_node = Node('new')
    
    # seed the list with a node
    subject.add(existing_node)

    # act
    actual = subject.add(new_node)

    # assert
    assert actual == 'new'
    assert subject == ['existing', 'new']


def test_ll_remove_empty_list():
    subject = LinkedList()

    with pytest.raises(NodeNotFoundException):
        subject.remove('dne')
